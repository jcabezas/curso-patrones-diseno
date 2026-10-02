# Glosario

Términos técnicos del curso, en orden alfabético. Cada módulo agrega los suyos.

## Abstracción

Un contrato general (normalmente una interfaz) que oculta los detalles de cada caso concreto. Quien la usa depende del contrato y no de las implementaciones.

Ver también: [módulo 03](teoria/03-ocp.md)

## Acoplamiento

Qué tanto depende un módulo de otro. Con acoplamiento bajo, cambiar una pieza no obliga a cambiar las demás.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Clase

Molde que define los datos y el comportamiento de un tipo de objeto. Un objeto es una instancia concreta de una clase.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Code smell

Señal en el código de que probablemente hay un problema de diseño, aunque el programa funcione (método largo, números mágicos, feature envy). Es una invitación a revisar, no un error.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Cohesión

Qué tanto trabajan en lo mismo las partes de un módulo. Una cohesión alta significa que una clase o función hace una sola cosa bien definida.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Composición

Técnica en la que un objeto se arma con otros objetos y les delega trabajo (relación "tiene un"). Es más flexible que la herencia.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Contrato

Conjunto de promesas que una clase o interfaz hace a quien la usa: qué precondiciones exige, qué poscondiciones garantiza y qué invariantes mantiene. Una subclase sustituible respeta el contrato de su base.

Ver también: [módulo 04](teoria/04-lsp.md)

## DRY

*Don't Repeat Yourself*: cada pieza de conocimiento (una regla, una fórmula) debe vivir en un solo lugar. No prohíbe que dos trozos de código se parezcan, solo que se repita la misma decisión.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Duck typing

En lenguajes dinámicos como Python, un objeto sirve si tiene los métodos que se le piden, sin importar su clase ("si camina como pato y suena como pato, es un pato"). Es polimorfismo sin declarar interfaces.

Ver también: [módulo 05](teoria/05-isp.md)

## Encapsulamiento

Ocultar el estado interno de un objeto y exponer solo operaciones controladas, de modo que el resto del código no dependa de los detalles.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Extensión

Agregar comportamiento nuevo escribiendo código nuevo (una clase que implementa una interfaz existente) sin editar el código que ya funciona.

Ver también: [módulo 03](teoria/03-ocp.md)

## God Object

Clase que lo sabe y lo hace todo: acumula muchas responsabilidades no relacionadas y todo el sistema depende de ella. Es la violación típica de SRP.

Ver también: [módulo 02](teoria/02-srp.md)

## Herencia

Mecanismo por el que una clase reutiliza y extiende a otra (relación "es un"). Es potente, pero acopla al hijo con el padre.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Interfaz

Contrato que lista las operaciones que un tipo promete ofrecer, sin decir cómo se implementan.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Interfaz gorda

Interfaz con demasiados métodos de motivos distintos, de los que cada cliente usa solo una parte. Obliga a las implementaciones a rellenar métodos que no les corresponden.

Ver también: [módulo 05](teoria/05-isp.md)

## Invariante

Condición que siempre es verdadera sobre un objeto, antes y después de cada operación (por ejemplo, un precio nunca negativo). Las subclases deben conservarla.

Ver también: [módulo 04](teoria/04-lsp.md)

## ISP

*Interface Segregation Principle*: ningún cliente debe verse obligado a depender de métodos que no usa. Se prefieren varias interfaces pequeñas y específicas a una sola interfaz gorda.

Ver también: [módulo 05](teoria/05-isp.md)

## KISS

*Keep It Simple, Stupid*: entre varias soluciones que resuelven el problema, elegir la más simple y fácil de entender.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Ley de Demeter

Un objeto solo debe hablar con sus vecinos inmediatos, no con los objetos de sus vecinos (`pedido.region_despacho()` en lugar de `pedido.cliente.direccion.comuna.region`). Reduce el acoplamiento.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## LSP

*Liskov Substitution Principle*: donde se espera un objeto de la clase base debe poder usarse una subclase sin que el programa se rompa ni se comporte de forma inesperada. Exige respetar el contrato de la base.

Ver también: [módulo 04](teoria/04-lsp.md)

## Magic number

Valor literal sin nombre dentro del código (`19`, `30`) cuyo significado nadie recuerda. Se corrige con una constante con nombre.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## OCP

*Open/Closed Principle*: el código debe estar abierto para extensión y cerrado para modificación. Los casos nuevos se agregan como código nuevo detrás de una abstracción, sin editar lo existente.

Ver también: [módulo 03](teoria/03-ocp.md)

## Patrón de diseño

Solución reutilizable y con nombre a un problema de diseño que se repite. Describe una estructura y cuándo aplicarla; no es código para copiar.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Polimorfismo

Capacidad de que un mismo mensaje produzca comportamientos distintos según el objeto que lo recibe.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Poscondición

Lo que un método garantiza que será verdad al terminar (por ejemplo, que el total devuelto no es negativo). Una subclase no puede debilitarla.

Ver también: [módulo 04](teoria/04-lsp.md)

## Precondición

Lo que debe cumplirse antes de llamar a un método para que funcione bien (por ejemplo, que el subtotal no sea negativo). Una subclase no puede endurecerla.

Ver también: [módulo 04](teoria/04-lsp.md)

## Razón para cambiar

Motivo de negocio, normalmente ligado a un área o persona, por el que hay que editar una clase. SRP pide que cada clase tenga una sola.

Ver también: [módulo 02](teoria/02-srp.md)

## Regla de tres

Heurística para abstraer: la primera vez se escribe, la segunda se tolera la repetición y a la tercera se extrae una abstracción, cuando ya se ve qué es común de verdad.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## SOLID

Cinco principios de diseño orientado a objetos (SRP, OCP, LSP, ISP, DIP) que ayudan a escribir código fácil de cambiar y de probar.

Ver también: [módulo 02](teoria/02-srp.md)

## SRP

*Single Responsibility Principle*: una clase debe tener una, y solo una, razón para cambiar. No significa que haga una sola cosa.

Ver también: [módulo 02](teoria/02-srp.md)

## UML

Lenguaje gráfico estándar para dibujar la estructura y el comportamiento del software. En el curso se escribe con Mermaid.

Ver también: [módulo 00](teoria/00-introduccion.md)

## YAGNI

*You Aren't Gonna Need It*: no implementar funcionalidad hasta que se necesite de verdad, porque lo construido "por si acaso" suele sobrar.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)
