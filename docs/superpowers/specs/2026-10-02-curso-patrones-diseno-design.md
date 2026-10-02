# Curso de patrones de diseño, SOLID y buenas prácticas — diseño

## Objetivo

Curso autodidacta en español neutro que explica de forma clara y simple los principios SOLID, las buenas prácticas de desarrollo y los 23 patrones GoF. Cada concepto lleva explicación, diagrama y código en Python, TypeScript, Go y PHP. Nivel entrevista: entender, saber explicar y reconocer cuándo usar (o no) cada cosa. No apunta a certificación.

## Decisiones (sesión 2026-10-02)

- **Alcance de patrones:** GoF completo (23): 5 creacionales, 7 estructurales, 11 de comportamiento. Sin patrones de arquitectura (CQRS, Hexagonal, etc.).
- **Código:** fragmentos dentro del Markdown, sin archivos ejecutables ni tests. Consecuencia: no hay garantía de compilación automática; se revisa a mano la coherencia entre los 4 lenguajes.
- **Dominio hilo conductor:** tienda online (carrito, pedidos, pagos, descuentos, notificaciones, inventario). Excepción: un patrón puede usar otro ejemplo solo si la tienda no lo representa de forma natural (p. ej. Composite con categorías ya cabe; Interpreter puede requerir un mini-lenguaje de reglas de descuento).
- **Estructura:** principios primero, catálogo después (enfoque A). Cada patrón se conecta con el principio SOLID que aplica o refuerza.
- **Lenguajes:** Python, TypeScript, Go, PHP. Go se escribe de forma idiomática (interfaces implícitas, embedding, funciones de primera clase) con una nota cuando un patrón se simplifica o casi desaparece (p. ej. Strategy como una función). *Asumido porque el usuario descartó la pregunta; modificable.*
- **Estilo:** español neutro (nunca voseo), diagramas Mermaid (labels con paréntesis entre comillas), términos técnicos con glosa de una frase en la primera aparición por módulo y enlace a `glosario.md`, término en inglés cuando es el estándar. Referencias entre módulos: hacia atrás enlace real, hacia adelante texto plano. Comandos en PowerShell, git en `main`.

## Estructura del repositorio

```
curso-patrones-diseno/
├── README.md                  # temario + checklist de estado (spec vivo)
├── glosario.md
├── preguntas-entrevista.md    # consolidado de todos los módulos
├── teoria/
│   ├── 00-introduccion.md
│   ├── 01-buenas-practicas.md
│   ├── 02-srp.md ... 06-dip.md
│   ├── 07-singleton.md ... (un archivo por patrón o grupo)
│   └── 20-antipatrones-y-cierre.md
└── docs/superpowers/specs/    # este spec
```

## Estructura fija de cada módulo de patrón

1. **El problema:** código "malo" en la tienda online.
2. **La idea en pocas palabras.**
3. **Diagrama Mermaid** (clases o secuencia).
4. **Código** en Python, TypeScript, Go y PHP (versión refactorizada).
5. **Cuándo usarlo / cuándo no**, y qué principio SOLID toca.
6. **Preguntas de entrevista.**

Los módulos de principios y buenas prácticas siguen el mismo esquema con "violación → refactor" en lugar de "problema → patrón".

## Temario

| Módulo | Contenido |
|---|---|
| 00 | Cómo usar el curso; repaso de OOP y diferencias entre los 4 lenguajes (interfaces, herencia, composición) |
| 01 | Buenas prácticas: DRY, KISS, YAGNI, nombres, funciones pequeñas, composición sobre herencia, ley de Demeter, manejo de errores, code smells |
| 02-06 | SOLID: SRP, OCP, LSP, ISP, DIP (un módulo cada uno) |
| 07-11 | Creacionales: Singleton, Factory Method, Abstract Factory, Builder, Prototype (un módulo cada uno) |
| 12-15 | Estructurales: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy (4 módulos agrupados) |
| 16-19 | Comportamiento: Strategy, Observer, Command, State, Template Method, Iterator, Chain of Responsibility, Mediator, Memento, Visitor, Interpreter (4 módulos agrupados) |
| 20 | Antipatrones, cuándo NO usar patrones, caso de cierre que combina varios en la tienda |

La agrupación exacta de los módulos 12-19 se fija en el plan de implementación.

## Verificación

Como no hay código ejecutable: revisión de enlaces (`glosario.md#...` y entre módulos), consistencia de la estructura fija por módulo, y que cada patrón tenga sus 4 lenguajes y su diagrama.

## Fuera de alcance

Patrones de arquitectura, concurrencia, funcionales, frameworks específicos, certificaciones.
