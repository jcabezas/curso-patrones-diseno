#!/usr/bin/env python3
"""Chequea la sintaxis de los bloques de código de teoria/*.md.

- Python: ast.parse
- PHP: php -l (agrega '<?php' si falta)
- TypeScript: transpileModule (instala typescript en .tmp/ la primera vez)
- Go: no se revisa automáticamente (no hay toolchain); revisar a mano

Cada bloque debe ser sintácticamente completo por sí solo.
Uso:  python scripts/sintaxis.py
"""
import ast
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from verificar import RAIZ, TEORIA, parsear  # noqa: E402

TMP = RAIZ / ".tmp"
JS_TS = """
const ts = require(process.argv[1]);
const bloques = JSON.parse(require("fs").readFileSync(0, "utf8"));
const res = bloques.map(b => {
  const r = ts.transpileModule(b, {reportDiagnostics: true,
    compilerOptions: {target: "ES2022", module: "ESNext"}});
  return (r.diagnostics || []).map(d => ts.flattenDiagnosticMessageText(d.messageText, "\\n"));
});
console.log(JSON.stringify(res));
"""


def bloques():
    for md in sorted(TEORIA.glob("[0-9]*.md")):
        for s in parsear(md.read_text(encoding="utf-8")):
            for lang, codigo in s["fences"]:
                yield md.name, s["titulo"], lang, codigo


def etiqueta(md, titulo, codigo):
    primera = next((l.strip() for l in codigo.splitlines() if l.strip()), "")
    return f"{md} > {titulo}: {primera[:50]}"


def revisar_python(items):
    errs = []
    for md, titulo, codigo in items:
        try:
            ast.parse(codigo)
        except SyntaxError as e:
            errs.append(f"{etiqueta(md, titulo, codigo)} -> {e.msg} (línea {e.lineno})")
    return errs


def revisar_php(items):
    php = shutil.which("php")
    if not php:
        print("aviso: php no está instalado, se omite PHP")
        return []
    errs = []
    for md, titulo, codigo in items:
        fuente = codigo if codigo.lstrip().startswith("<?php") else "<?php\n" + codigo
        with tempfile.NamedTemporaryFile("w", suffix=".php", delete=False, encoding="utf-8") as f:
            f.write(fuente)
        r = subprocess.run([php, "-l", f.name], capture_output=True, text=True)
        pathlib.Path(f.name).unlink()
        if r.returncode != 0:
            msg = (r.stdout + r.stderr).strip().splitlines()[0]
            errs.append(f"{etiqueta(md, titulo, codigo)} -> {msg}")
    return errs


def revisar_typescript(items):
    node, npm = shutil.which("node"), shutil.which("npm")
    if not (node and npm):
        print("aviso: node/npm no están instalados, se omite TypeScript")
        return []
    modulo = TMP / "node_modules" / "typescript"
    if not modulo.exists():
        TMP.mkdir(exist_ok=True)
        subprocess.run([npm, "install", "--prefix", str(TMP), "typescript@5",
                        "--no-audit", "--no-fund", "--silent"], check=True)
    r = subprocess.run([node, "-e", JS_TS, str(modulo)], capture_output=True, text=True,
                       input=json.dumps([c for _, _, c in items]))
    if r.returncode != 0:
        return [f"typescript: {r.stderr.strip()[:200]}"]
    resultado = json.loads(r.stdout)
    return [f"{etiqueta(md, titulo, codigo)} -> {d}"
            for (md, titulo, codigo), diags in zip(items, resultado) for d in diags]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    por_lang = {"python": [], "php": [], "typescript": []}
    n_go = 0
    for md, titulo, lang, codigo in bloques():
        if lang in por_lang:
            por_lang[lang].append((md, titulo, codigo))
        elif lang == "go":
            n_go += 1
    errs = (revisar_python(por_lang["python"]) + revisar_php(por_lang["php"])
            + revisar_typescript(por_lang["typescript"]))
    for e in errs:
        print("ERR", e)
    print(f"revisados: {len(por_lang['python'])} python, {len(por_lang['php'])} php, "
          f"{len(por_lang['typescript'])} typescript; {n_go} bloques go sin revisar (manual)")
    print(f"{len(errs)} error(es)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
