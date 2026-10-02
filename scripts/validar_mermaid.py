#!/usr/bin/env python3
"""Genera .tmp/mermaid-check.html para validar todos los diagramas en un navegador.

Uso:
    python scripts/validar_mermaid.py
    python -m http.server 8765 --bind 127.0.0.1 --directory .tmp
    # abrir http://127.0.0.1:8765/mermaid-check.html; la página lista OK/ERR por diagrama
    # (no funciona como file://; necesita internet para cargar mermaid desde jsdelivr)
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from verificar import RAIZ, TEORIA, parsear  # noqa: E402

HTML = """<!doctype html>
<meta charset="utf-8"><title>Validación Mermaid</title>
<h1 id="resumen">validando...</h1>
<pre id="detalle"></pre>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({startOnLoad: false});
const bloques = __BLOQUES__;
let errores = 0, lineas = [];
for (const b of bloques) {
  try { await mermaid.parse(b.codigo); lineas.push("OK  " + b.donde); }
  catch (e) { errores++; lineas.push("ERR " + b.donde + " -> " + String(e.message || e).split("\\n")[0]); }
}
document.getElementById("detalle").textContent = lineas.join("\\n");
document.getElementById("resumen").textContent =
  "RESULTADO: " + bloques.length + " diagramas, " + errores + " con error";
</script>
"""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    bloques = []
    for md in sorted(TEORIA.glob("[0-9]*.md")):
        for s in parsear(md.read_text(encoding="utf-8")):
            for lang, codigo in s["fences"]:
                if lang == "mermaid":
                    bloques.append({"donde": f"{md.name} > {s['titulo']}", "codigo": codigo})
    destino = RAIZ / ".tmp" / "mermaid-check.html"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(HTML.replace("__BLOQUES__", json.dumps(bloques)), encoding="utf-8")
    print(f"{len(bloques)} diagramas -> {destino}")


if __name__ == "__main__":
    main()
