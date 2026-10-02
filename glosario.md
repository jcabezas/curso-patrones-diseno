# Glosario

Términos técnicos del curso, en orden alfabético. Cada módulo agrega los suyos.

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

## DRY

*Don't Repeat Yourself*: cada pieza de conocimiento (una regla, una fórmula) debe vivir en un solo lugar. No prohíbe que dos trozos de código se parezcan, solo que se repita la misma decisión.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Encapsulamiento

Ocultar el estado interno de un objeto y exponer solo operaciones controladas, de modo que el resto del código no dependa de los detalles.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Herencia

Mecanismo por el que una clase reutiliza y extiende a otra (relación "es un"). Es potente, pero acopla al hijo con el padre.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Interfaz

Contrato que lista las operaciones que un tipo promete ofrecer, sin decir cómo se implementan.

Ver también: [módulo 00](teoria/00-introduccion.md)

## KISS

*Keep It Simple, Stupid*: entre varias soluciones que resuelven el problema, elegir la más simple y fácil de entender.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Ley de Demeter

Un objeto solo debe hablar con sus vecinos inmediatos, no con los objetos de sus vecinos (`pedido.region_despacho()` en lugar de `pedido.cliente.direccion.comuna.region`). Reduce el acoplamiento.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Magic number

Valor literal sin nombre dentro del código (`19`, `30`) cuyo significado nadie recuerda. Se corrige con una constante con nombre.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Patrón de diseño

Solución reutilizable y con nombre a un problema de diseño que se repite. Describe una estructura y cuándo aplicarla; no es código para copiar.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Polimorfismo

Capacidad de que un mismo mensaje produzca comportamientos distintos según el objeto que lo recibe.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Regla de tres

Heurística para abstraer: la primera vez se escribe, la segunda se tolera la repetición y a la tercera se extrae una abstracción, cuando ya se ve qué es común de verdad.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## UML

Lenguaje gráfico estándar para dibujar la estructura y el comportamiento del software. En el curso se escribe con Mermaid.

Ver también: [módulo 00](teoria/00-introduccion.md)

## YAGNI

*You Aren't Gonna Need It*: no implementar funcionalidad hasta que se necesite de verdad, porque lo construido "por si acaso" suele sobrar.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)
