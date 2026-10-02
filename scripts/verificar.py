#!/usr/bin/env python3
"""Verifica la estructura de los módulos del curso.

Uso:
    python scripts/verificar.py --modulo 7    # un módulo
    python scripts/verificar.py               # todos los módulos + enlaces
    python scripts/verificar.py --final       # lo anterior + README, glosario y preguntas
"""
import argparse
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TEORIA = RAIZ / "teoria"
LENGUAJES = ["Python", "TypeScript", "Go", "PHP"]
FENCE = {"Python": "python", "TypeScript": "typescript", "Go": "go", "PHP": "php"}

# número -> (archivo, tipo, patrones GoF que debe contener)
MODULOS = {
    0: ("00-introduccion", "intro", []),
    1: ("01-buenas-practicas", "intro", []),
    2: ("02-srp", "solid", []),
    3: ("03-ocp", "solid", []),
    4: ("04-lsp", "solid", []),
    5: ("05-isp", "solid", []),
    6: ("06-dip", "solid", []),
    7: ("07-singleton", "patron", ["Singleton"]),
    8: ("08-factory-method", "patron", ["Factory Method"]),
    9: ("09-abstract-factory", "patron", ["Abstract Factory"]),
    10: ("10-builder", "patron", ["Builder"]),
    11: ("11-prototype", "patron", ["Prototype"]),
    12: ("12-adapter-facade", "patron", ["Adapter", "Facade"]),
    13: ("13-decorator-proxy", "patron", ["Decorator", "Proxy"]),
    14: ("14-composite-flyweight", "patron", ["Composite", "Flyweight"]),
    15: ("15-bridge", "patron", ["Bridge"]),
    16: ("16-strategy-state-template-method", "patron",
         ["Strategy", "State", "Template Method"]),
    17: ("17-observer-mediator-chain", "patron",
         ["Observer", "Mediator", "Chain of Responsibility"]),
    18: ("18-command-memento-iterator", "patron",
         ["Command", "Memento", "Iterator"]),
    19: ("19-visitor-interpreter", "patron", ["Visitor", "Interpreter"]),
    20: ("20-antipatrones-y-cierre", "cierre", []),
}

PREGUNTAS = "Preguntas de entrevista"
H3_PATRON = ["El problema", "La idea en pocas palabras", "Diagrama", "Código",
             "Cuándo usarlo y cuándo no"]
H2_SOLID = ["La violación", "La idea en pocas palabras", "Diagrama", "Código",
            "Cuándo aplicarlo y cuándo no", "Ejercicio: detecta la violación",
            PREGUNTAS]
H2_CIERRE = ["Antipatrones", "Cuándo no usar patrones", "Caso de cierre", PREGUNTAS]
H2_NO_PATRON = {PREGUNTAS, "Comparación", "Resumen"}
SOLID_RE = re.compile(r"\b(SRP|OCP|LSP|ISP|DIP)\b")
VOSEO_RE = re.compile(
    r"\b(vos|tenés|podés|querés|sabés|grabás|parás|hacé|mirá|fijate|usá|ponés|"
    r"decís|sos|andá|elegí|pensá|escribí|aplicá|fijá)\b", re.I)
PREGUNTA_RE = re.compile(r"^\*\*P\d+\.")


def parsear(texto):
    """Divide el Markdown en secciones; los bloques de código quedan aparte."""
    secs = [{"nivel": 0, "titulo": "", "lineas": [], "fences": []}]
    en_fence, lang, buf = False, "", []
    for linea in texto.splitlines():
        if en_fence:
            if linea.startswith("```"):
                secs[-1]["fences"].append((lang, "\n".join(buf)))
                en_fence = False
            else:
                buf.append(linea)
            continue
        if linea.startswith("```"):
            en_fence, lang, buf = True, linea[3:].strip().lower(), []
            continue
        h = re.match(r"^(#{1,6}) +(.*?)\s*$", linea)
        if h:
            secs.append({"nivel": len(h.group(1)), "titulo": h.group(2),
                         "lineas": [], "fences": []})
        else:
            secs[-1]["lineas"].append(linea)
    return secs


def rango(secs, i):
    """La sección i y todas sus subsecciones."""
    fin = i + 1
    while fin < len(secs) and secs[fin]["nivel"] > secs[i]["nivel"]:
        fin += 1
    return secs[i:fin]


def titulos(sub, nivel):
    return [s["titulo"] for s in sub if s["nivel"] == nivel]


def fences(sub, lang):
    return sum(1 for s in sub for (l, _) in s["fences"] if l == lang)


def revisar_lenguajes(sub, etiqueta, minimo_python, errs):
    for leng in LENGUAJES:
        minimo = minimo_python if leng == "Python" else 1
        n = fences(sub, FENCE[leng])
        if n < minimo:
            errs.append(f"{etiqueta}: {n} bloque(s) {FENCE[leng]}, mínimo {minimo}")


def revisar_preguntas(secs, errs):
    idx = [i for i, s in enumerate(secs) if s["nivel"] == 2 and s["titulo"] == PREGUNTAS]
    if not idx:
        errs.append(f"falta la sección '## {PREGUNTAS}'")
        return
    lineas = [l for s in rango(secs, idx[0]) for l in s["lineas"]]
    n = sum(1 for l in lineas if PREGUNTA_RE.match(l))
    if not 4 <= n <= 6:
        errs.append(f"{PREGUNTAS}: {n} preguntas con formato '**P1. ...**', se esperan 4 a 6")


def revisar_mermaid(secs, errs):
    mermaid = [c for s in secs for (l, c) in s["fences"] if l == "mermaid"]
    for c in mermaid:
        if c.lstrip().startswith(("flowchart", "graph")) and \
                re.search(r'\[[^\]"]*[()][^\]"]*\]', c):
            errs.append("mermaid: label con paréntesis sin comillas en un flowchart")
    return len(mermaid)


def errores_modulo(num):
    nombre, tipo, patrones = MODULOS[num]
    ruta = TEORIA / f"{nombre}.md"
    if not ruta.exists():
        return [f"falta teoria/{nombre}.md"]
    secs = parsear(ruta.read_text(encoding="utf-8"))
    errs = []
    if not any(s["nivel"] == 1 for s in secs):
        errs.append("falta el título '# ...'")
    n_mermaid = revisar_mermaid(secs, errs)
    revisar_preguntas(secs, errs)

    if tipo == "patron":
        bloques = [i for i, s in enumerate(secs)
                   if s["nivel"] == 2 and s["titulo"] not in H2_NO_PATRON]
        nombres = [secs[i]["titulo"] for i in bloques]
        for p in patrones:
            if p not in nombres:
                errs.append(f"falta el patrón '## {p}'")
        for n in nombres:
            if n not in patrones:
                errs.append(f"sección '## {n}' no es un patrón esperado en este módulo")
        for i in bloques:
            sub = rango(secs, i)
            et = secs[i]["titulo"]
            for h in H3_PATRON:
                if h not in titulos(sub, 3):
                    errs.append(f"{et}: falta '### {h}'")
            codigo = [j for j, s in enumerate(sub) if s["nivel"] == 3 and s["titulo"] == "Código"]
            if codigo:
                hijos = rango(sub, codigo[0])
                for leng in LENGUAJES:
                    if leng not in titulos(hijos, 4):
                        errs.append(f"{et}: falta '#### {leng}' en Código")
            revisar_lenguajes(sub, et, 2, errs)
            if fences(sub, "mermaid") < 1:
                errs.append(f"{et}: falta el diagrama mermaid")
            cuando = [s for s in sub if s["titulo"] == "Cuándo usarlo y cuándo no"]
            if cuando and not SOLID_RE.search(" ".join(cuando[0]["lineas"])):
                errs.append(f"{et}: 'Cuándo usarlo...' no nombra un principio SOLID (SRP/OCP/LSP/ISP/DIP)")
    elif tipo == "solid":
        h2 = titulos(secs, 2)
        for h in H2_SOLID:
            if h not in h2:
                errs.append(f"falta '## {h}'")
        codigo = [i for i, s in enumerate(secs) if s["nivel"] == 2 and s["titulo"] == "Código"]
        if codigo:
            hijos = rango(secs, codigo[0])
            for leng in LENGUAJES:
                if leng not in titulos(hijos, 3):
                    errs.append(f"falta '### {leng}' en Código")
        revisar_lenguajes(secs, "módulo", 2, errs)
        if n_mermaid < 1:
            errs.append("falta el diagrama mermaid")
    else:  # intro y cierre
        if tipo == "cierre":
            for h in H2_CIERRE:
                if h not in titulos(secs, 2):
                    errs.append(f"falta '## {h}'")
        revisar_lenguajes(secs, "módulo", 1, errs)
        if n_mermaid < 1:
            errs.append("falta el diagrama mermaid")

    for s in secs:
        for l in s["lineas"]:
            m = VOSEO_RE.search(l)
            if m:
                errs.append(f"voseo: '{m.group(0)}' en: {l.strip()[:60]}")
    return errs


def slug(titulo):
    return re.sub(r"[^\w\- ]", "", titulo.lower().replace("`", "")).replace(" ", "-")


def anclas(ruta):
    secs = parsear(ruta.read_text(encoding="utf-8"))
    return {slug(s["titulo"]) for s in secs if s["nivel"] >= 1}


def errores_enlaces():
    errs = []
    archivos = list(RAIZ.glob("*.md")) + list(TEORIA.glob("*.md"))
    for md in archivos:
        texto = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
        for destino in re.findall(r"\]\(([^)\s]+)\)", texto):
            if destino.startswith(("http://", "https://", "mailto:")):
                continue
            ruta, _, ancla = destino.partition("#")
            objetivo = md if not ruta else (md.parent / ruta).resolve()
            if not objetivo.exists():
                errs.append(f"{md.name}: enlace roto a {destino}")
            elif ancla and objetivo.suffix == ".md" and ancla not in anclas(objetivo):
                errs.append(f"{md.name}: ancla inexistente en {destino}")
    return errs


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--modulo", type=int)
    ap.add_argument("--final", action="store_true")
    args = ap.parse_args()
    nums = [args.modulo] if args.modulo is not None else sorted(MODULOS)
    total = 0
    for n in nums:
        errs = errores_modulo(n)
        total += len(errs)
        print(f"[{'OK ' if not errs else 'ERR'}] módulo {n:02d} {MODULOS[n][0]}")
        for e in errs:
            print(f"      - {e}")
    if args.modulo is None:
        enl = errores_enlaces()
        total += len(enl)
        print(f"[{'OK ' if not enl else 'ERR'}] enlaces")
        for e in enl:
            print(f"      - {e}")
    if args.final:
        for f in ["README.md", "glosario.md", "preguntas-entrevista.md"]:
            if not (RAIZ / f).exists():
                total += 1
                print(f"[ERR] falta {f}")
    print(f"\n{total} error(es)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
