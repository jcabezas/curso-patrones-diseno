#!/usr/bin/env python3
"""Genera preguntas-entrevista.md juntando la sección de preguntas de cada módulo.

Las preguntas transversales (que cruzan módulos) viven en
teoria/_transversales.md y se anexan al final.

Uso:  python scripts/consolidar_preguntas.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from verificar import MODULOS, PREGUNTAS, RAIZ, TEORIA  # noqa: E402

GRUPOS = [
    ("Introducción y buenas prácticas", [0, 1]),
    ("Principios SOLID", [2, 3, 4, 5, 6]),
    ("Patrones creacionales", [7, 8, 9, 10, 11]),
    ("Patrones estructurales", [12, 13, 14, 15]),
    ("Patrones de comportamiento", [16, 17, 18, 19]),
    ("Antipatrones y cierre", [20]),
]


def extraer(num):
    nombre = MODULOS[num][0]
    texto = (TEORIA / f"{nombre}.md").read_text(encoding="utf-8")
    titulo = re.search(r"(?m)^# (.+)$", texto).group(1).strip()
    m = re.search(rf"(?ms)^## {re.escape(PREGUNTAS)}\s*\n(.*?)(?=^## |\Z)", texto)
    if not m:
        raise SystemExit(f"módulo {num:02d}: no tiene '## {PREGUNTAS}'")
    return nombre, titulo, m.group(1).strip()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    out = ["# Preguntas de entrevista\n",
           "> Archivo generado por `scripts/consolidar_preguntas.py`. "
           "No editar a mano: edita la sección de preguntas del módulo.\n"]
    for grupo, nums in GRUPOS:
        out.append(f"\n## {grupo}\n")
        for n in nums:
            nombre, titulo, cuerpo = extraer(n)
            out.append(f"\n### {titulo} ([módulo {n:02d}](teoria/{nombre}.md))\n\n{cuerpo}\n")
    transv = TEORIA / "_transversales.md"
    if transv.exists():
        out.append("\n## Preguntas transversales\n\n" + transv.read_text(encoding="utf-8").strip() + "\n")
    destino = RAIZ / "preguntas-entrevista.md"
    destino.write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"escrito {destino.name}")


if __name__ == "__main__":
    main()
