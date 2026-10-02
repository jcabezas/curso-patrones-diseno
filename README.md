# Curso de patrones de diseño, SOLID y buenas prácticas

Curso autodidacta, nivel entrevista: entender cada concepto, saber explicarlo y reconocer cuándo usarlo. Todos los ejemplos usan una **tienda online** y están en **Python, TypeScript, Go y PHP**. Cada concepto trae una explicación simple, un diagrama Mermaid y preguntas de entrevista.

## Cómo está organizado

- `teoria/` — un módulo por archivo, en el orden del temario.
- `glosario.md` — términos técnicos.
- `preguntas-entrevista.md` — todas las preguntas juntas (generado).

## Convenciones

- Dinero en pesos chilenos como entero (`12990`).
- Dominio fijo: `Producto`, `ItemCarrito`, `Carrito`, `Cliente`, `Pedido`, `MetodoPago`, `ReglaDescuento`, `Notificador`, `PedidoRepository`.
- Cada patrón sigue el mismo orden: El problema, La idea en pocas palabras, Diagrama, Código, Cuándo usarlo y cuándo no, Preguntas de entrevista.
- Go se escribe de forma idiomática; cuando un patrón casi desaparece en Go, hay una nota.

## Temario y estado

- [x] 00 [Introducción y repaso de OOP](teoria/00-introduccion.md)
- [x] 01 [Buenas prácticas](teoria/01-buenas-practicas.md)
- [x] 02 [SRP](teoria/02-srp.md)
- [x] 03 [OCP](teoria/03-ocp.md)
- [x] 04 [LSP](teoria/04-lsp.md)
- [x] 05 [ISP](teoria/05-isp.md)
- [x] 06 [DIP](teoria/06-dip.md)
- [x] 07 [Singleton](teoria/07-singleton.md)
- [x] 08 [Factory Method](teoria/08-factory-method.md)
- [x] 09 [Abstract Factory](teoria/09-abstract-factory.md)
- [x] 10 [Builder](teoria/10-builder.md)
- [x] 11 [Prototype](teoria/11-prototype.md)
- [x] 12 [Adapter y Facade](teoria/12-adapter-facade.md)
- [ ] 13 [Decorator y Proxy](teoria/13-decorator-proxy.md)
- [ ] 14 [Composite y Flyweight](teoria/14-composite-flyweight.md)
- [ ] 15 [Bridge](teoria/15-bridge.md)
- [ ] 16 [Strategy, State y Template Method](teoria/16-strategy-state-template-method.md)
- [ ] 17 [Observer, Mediator y Chain of Responsibility](teoria/17-observer-mediator-chain.md)
- [ ] 18 [Command, Memento e Iterator](teoria/18-command-memento-iterator.md)
- [ ] 19 [Visitor e Interpreter](teoria/19-visitor-interpreter.md)
- [ ] 20 [Antipatrones y caso de cierre](teoria/20-antipatrones-y-cierre.md)

## Verificación (para quien mantiene el curso)

```bash
python scripts/verificar.py            # estructura, lenguajes, diagramas, enlaces, voseo
python scripts/sintaxis.py             # sintaxis de Python, PHP y TypeScript
python scripts/consolidar_preguntas.py # regenera preguntas-entrevista.md
python scripts/validar_mermaid.py      # genera .tmp/mermaid-check.html (ver docstring)
```
