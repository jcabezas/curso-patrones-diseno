# Glosario

Términos técnicos del curso, en orden alfabético. Cada módulo agrega los suyos.

## Abstracción

Tiene dos acepciones en el curso.

1. General: un contrato (normalmente una interfaz) que oculta los detalles de cada caso concreto. Quien la usa depende del contrato y no de las implementaciones.
2. En el patrón Bridge (GoF): la clase de alto nivel que delega el trabajo en un implementor (por ejemplo, `Aviso`, que delega en un `Canal`). No es una interfaz ni una clase abstracta, aunque el nombre lo sugiera; puede ser una clase concreta.

Ver también: [módulo 03](teoria/03-ocp.md), [módulo 15](teoria/15-bridge.md)

## Abstract Factory

Patrón creacional que ofrece una interfaz con un método de creación por cada producto de una familia. Cada fábrica concreta devuelve las piezas de su propia familia, así que el cliente no puede mezclar piezas incompatibles.

Ver también: [módulo 09](teoria/09-abstract-factory.md)

## Acoplamiento

Qué tanto depende un módulo de otro. Con acoplamiento bajo, cambiar una pieza no obliga a cambiar las demás.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Adapter

Patrón estructural que convierte la interfaz de una clase existente en la que el cliente espera, envolviéndola y traduciendo datos de entrada y de salida. Sirve para integrar SDK o código que no se puede modificar.

Ver también: [módulo 12](teoria/12-adapter-facade.md)

## Árbol

Estructura de datos en la que cada elemento (nodo) puede tener elementos hijos, empezando por una raíz. Las carpetas con archivos y los combos con productos son ejemplos.

Ver también: [módulo 14](teoria/14-composite-flyweight.md)

## Bridge

Patrón estructural que separa una abstracción de su implementación en dos jerarquías independientes. La abstracción guarda una referencia al implementor y le delega el trabajo, así que cada lado crece sin tocar al otro.

Ver también: [módulo 15](teoria/15-bridge.md)

## Builder

Patrón creacional que arma un objeto complejo paso a paso y lo entrega al final con `construir()`, ya validado. Evita constructores con muchos parámetros y objetos a medio armar.

Ver también: [módulo 10](teoria/10-builder.md)

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

## Composite

Patrón estructural que compone objetos en un árbol y permite tratar de la misma forma a un objeto individual (hoja) y a un grupo de ellos (compuesto) mediante una interfaz común.

Ver también: [módulo 14](teoria/14-composite-flyweight.md)

## Composition root

Único lugar, cerca del arranque del programa, que conoce las clases concretas, las crea y las conecta entre sí. El resto del código solo ve interfaces.

Ver también: [módulo 06](teoria/06-dip.md)

## Constructor telescópico

Constructor con una larga fila de parámetros opcionales que crece con cada opción nueva. Es fácil pasar un valor en la posición equivocada y no hay dónde validar el conjunto.

Ver también: [módulo 10](teoria/10-builder.md)

## Contrato

Conjunto de promesas que una clase o interfaz hace a quien la usa: qué precondiciones exige, qué poscondiciones garantiza y qué invariantes mantiene. Una subclase sustituible respeta el contrato de su base.

Ver también: [módulo 04](teoria/04-lsp.md)

## Copia profunda

Copia de un objeto que duplica también todo lo que contiene (listas, objetos internos), recursivamente. El clon es independiente: modificarlo no afecta al original.

Ver también: [módulo 11](teoria/11-prototype.md)

## Copia superficial

Copia de un objeto que duplica solo el objeto, pero deja sus campos de referencia (listas, maps, objetos internos) apuntando a los mismos objetos del original. Modificar uno de esos campos en el clon también cambia el original.

Ver también: [módulo 11](teoria/11-prototype.md)

## Decorator

Patrón estructural que envuelve un objeto para agregarle comportamiento en tiempo de ejecución, manteniendo la misma interfaz, de modo que se pueden apilar varios.

Ver también: [módulo 13](teoria/13-decorator-proxy.md)

## DIP

*Dependency Inversion Principle*: los módulos de alto nivel no deben depender de los de bajo nivel; ambos deben depender de abstracciones. La regla define el contrato y el detalle lo implementa.

Ver también: [módulo 06](teoria/06-dip.md)

## DRY

*Don't Repeat Yourself*: cada pieza de conocimiento (una regla, una fórmula) debe vivir en un solo lugar. No prohíbe que dos trozos de código se parezcan, solo que se repita la misma decisión.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Duck typing

En lenguajes dinámicos como Python, un objeto sirve si tiene los métodos que se le piden, sin importar su clase ("si camina como pato y suena como pato, es un pato"). Es polimorfismo sin declarar interfaces.

Ver también: [módulo 05](teoria/05-isp.md)

## Encapsulamiento

Ocultar el estado interno de un objeto y exponer solo operaciones controladas, de modo que el resto del código no dependa de los detalles.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Estado extrínseco

En Flyweight, la parte del estado que depende de cada uso del objeto (como el SKU y el precio de un ítem). No se comparte: lo guarda el contexto o se pasa como argumento.

Ver también: [módulo 14](teoria/14-composite-flyweight.md)

## Estado global

Datos que cualquier parte del programa puede leer o modificar desde cualquier lugar (una variable global, un Singleton mutable). Esconde dependencias y hace que las pruebas se contaminen entre sí.

Ver también: [módulo 07](teoria/07-singleton.md)

## Estado intrínseco

En Flyweight, la parte del estado que es igual para muchos objetos y no cambia (como la descripción y la imagen de un tipo de producto). Es inmutable y se comparte.

Ver también: [módulo 14](teoria/14-composite-flyweight.md)

## Explosión de subclases

Crecimiento del número de clases como el producto de dos variaciones independientes (2 tipos de aviso por 3 canales son 6 clases) cuando se resuelven con herencia. Bridge lo reduce a una suma.

Ver también: [módulo 15](teoria/15-bridge.md)

## Extensión

Agregar comportamiento nuevo escribiendo código nuevo (una clase que implementa una interfaz existente) sin editar el código que ya funciona.

Ver también: [módulo 03](teoria/03-ocp.md)

## Facade

Patrón estructural que ofrece una interfaz simple y unificada sobre un subsistema complejo, coordinando sus piezas en el orden correcto. No impide usar el subsistema directamente.

Ver también: [módulo 12](teoria/12-adapter-facade.md)

## Factory Method

Patrón creacional que define un método creador en una clase base y deja que las subclases decidan qué clase concreta instanciar. En lenguajes sin herencia, como Go, se reduce a una función constructora que devuelve una interfaz.

Ver también: [módulo 08](teoria/08-factory-method.md)

## Familia de productos

Conjunto de objetos pensados para usarse juntos, como Webpay, el antifraude local y la boleta SII en Chile. Una Abstract Factory crea una familia completa y evita mezclar piezas de familias distintas.

Ver también: [módulo 09](teoria/09-abstract-factory.md)

## Flyweight

Patrón estructural que ahorra memoria compartiendo la parte común e inmutable (estado intrínseco) de muchos objetos, y guardando aparte la parte que varía (estado extrínseco).

Ver también: [módulo 14](teoria/14-composite-flyweight.md)

## Functional options

Idioma de Go para construir objetos con opciones: la función constructora recibe los datos obligatorios y una lista variable de funciones que modifican el objeto (`NuevoPedido(cliente, ConCupon("X"))`). Reemplaza al Builder clásico.

Ver también: [módulo 10](teoria/10-builder.md)

## God Object

Clase que lo sabe y lo hace todo: acumula muchas responsabilidades no relacionadas y todo el sistema depende de ella. Es la violación típica de SRP.

Ver también: [módulo 02](teoria/02-srp.md)

## Herencia

Mecanismo por el que una clase reutiliza y extiende a otra (relación "es un"). Es potente, pero acopla al hijo con el padre.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Hook

Paso de un algoritmo con una implementación por defecto que las subclases (o quien lo configura) pueden sobrescribir, pero no están obligadas a ello. En Template Method se distingue de los pasos abstractos, que sí son obligatorios.

Ver también: [módulo 16](teoria/16-strategy-state-template-method.md)

## Implementor

En Bridge, la interfaz de bajo nivel que hace el trabajo real y a la que la abstracción delega (por ejemplo, `Canal` para entregar un aviso). Sus implementaciones concretas son intercambiables.

Ver también: [módulo 15](teoria/15-bridge.md)

## Interfaz

Contrato que lista las operaciones que un tipo promete ofrecer, sin decir cómo se implementan.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Interfaz fluida

Estilo de API en que cada método devuelve el propio objeto, de modo que las llamadas se encadenan y se leen casi como una frase (`b.conCliente(x).conCupon(y).construir()`).

Ver también: [módulo 10](teoria/10-builder.md)

## Interfaz gorda

Interfaz con demasiados métodos de motivos distintos, de los que cada cliente usa solo una parte. Obliga a las implementaciones a rellenar métodos que no les corresponden.

Ver también: [módulo 05](teoria/05-isp.md)

## Inyección de dependencias

Técnica en la que una clase recibe de afuera las piezas que necesita (por constructor, método o propiedad) en lugar de crearlas ella misma. Es la forma más común de cumplir DIP.

Ver también: [módulo 06](teoria/06-dip.md)

## Invariante

Condición que siempre es verdadera sobre un objeto, antes y después de cada operación (por ejemplo, un precio nunca negativo). Las subclases deben conservarla.

Ver también: [módulo 04](teoria/04-lsp.md)

## IoC

*Inversion of Control*: el control de crear y conectar los objetos lo tiene un marco o contenedor, no tu código. Un contenedor de IoC automatiza la inyección de dependencias y es opcional.

Ver también: [módulo 06](teoria/06-dip.md)

## ISP

*Interface Segregation Principle*: ningún cliente debe verse obligado a depender de métodos que no usa. Se prefieren varias interfaces pequeñas y específicas a una sola interfaz gorda.

Ver también: [módulo 05](teoria/05-isp.md)

## KISS

*Keep It Simple, Stupid*: entre varias soluciones que resuelven el problema, elegir la más simple y fácil de entender.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Lazy loading

Carga diferida: crear u obtener un recurso costoso solo cuando se usa por primera vez, no al inicio. Un proxy virtual es una forma de implementarla.

Ver también: [módulo 13](teoria/13-decorator-proxy.md)

## Ley de Demeter

Un objeto solo debe hablar con sus vecinos inmediatos, no con los objetos de sus vecinos (`pedido.region_despacho()` en lugar de `pedido.cliente.direccion.comuna.region`). Reduce el acoplamiento.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## LSP

*Liskov Substitution Principle*: donde se espera un objeto de la clase base debe poder usarse una subclase sin que el programa se rompa ni se comporte de forma inesperada. Exige respetar el contrato de la base.

Ver también: [módulo 04](teoria/04-lsp.md)

## Magic number

Valor literal sin nombre dentro del código (`19`, `30`) cuyo significado nadie recuerda. Se corrige con una constante con nombre.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Máquina de estados

Modelo de un objeto como un conjunto de estados y las transiciones permitidas entre ellos (`Pendiente` → `Pagado` → `Enviado`). Las transiciones que no existen en el modelo se rechazan. State es su implementación orientada a objetos.

Ver también: [módulo 16](teoria/16-strategy-state-template-method.md)

## Método creador

El método de un Factory Method que crea y devuelve el producto (por ejemplo `crearNotificador()`). La clase base lo declara y cada subclase lo sobrescribe para elegir qué clase concreta se instancia.

Ver también: [módulo 08](teoria/08-factory-method.md)

## Middleware

Función o componente que envuelve al manejador de una petición para hacer algo antes y después (autenticar, registrar, medir) y luego delegar en el siguiente. Es un Decorator aplicado a funciones.

Ver también: [módulo 13](teoria/13-decorator-proxy.md)

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

## Prototype

Patrón creacional que crea objetos copiando un objeto existente mediante un método `clonar()`, sin conocer su clase concreta ni sus campos. Lo delicado es que la copia sea profunda.

Ver también: [módulo 11](teoria/11-prototype.md)

## Principio de Hollywood

"No nos llames, te llamamos": el código de alto nivel llama al de bajo nivel y no al revés. Es la forma de inversión de control que usan Template Method y los frameworks.

Ver también: [módulo 16](teoria/16-strategy-state-template-method.md)

## Proxy

Patrón estructural que ofrece un sustituto con la misma interfaz que el objeto real y controla el acceso a él (caché, carga diferida, permisos, registro).

Ver también: [módulo 13](teoria/13-decorator-proxy.md)

## Razón para cambiar

Motivo de negocio, normalmente ligado a un área o persona, por el que hay que editar una clase. SRP pide que cada clase tenga una sola.

Ver también: [módulo 02](teoria/02-srp.md)

## Regla de tres

Heurística para abstraer: la primera vez se escribe, la segunda se tolera la repetición y a la tercera se extrae una abstracción, cuando ya se ve qué es común de verdad.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)

## Simple Factory

Función o clase con un método que construye objetos según un parámetro (por ejemplo `crearNotificador("sms")`). No es un patrón GoF, pero es la forma más común de centralizar la creación.

Ver también: [módulo 08](teoria/08-factory-method.md)

## Singleton

Patrón creacional que garantiza que una clase tenga una única instancia y ofrece un punto de acceso global a ella. Casi siempre es preferible crear una instancia única en el composition root e inyectarla.

Ver también: [módulo 07](teoria/07-singleton.md)

## SOLID

Cinco principios de diseño orientado a objetos (SRP, OCP, LSP, ISP, DIP) que ayudan a escribir código fácil de cambiar y de probar.

Ver también: [módulo 02](teoria/02-srp.md)

## SRP

*Single Responsibility Principle*: una clase debe tener una, y solo una, razón para cambiar. No significa que haga una sola cosa.

Ver también: [módulo 02](teoria/02-srp.md)

## State

Patrón de comportamiento que permite a un objeto cambiar su comportamiento cuando cambia su estado interno, delegando en un objeto por cada estado. Cada estado devuelve el siguiente o rechaza la transición.

Ver también: [módulo 16](teoria/16-strategy-state-template-method.md)

## Strategy

Patrón de comportamiento que encapsula una familia de algoritmos intercambiables detrás de una interfaz común, de modo que el cliente elige cuál usar en tiempo de ejecución.

Ver también: [módulo 16](teoria/16-strategy-state-template-method.md)

## Subsistema

Conjunto de clases que colaboran para una tarea y tienen interfaces propias; una fachada se pone delante de él para simplificar su uso.

Ver también: [módulo 12](teoria/12-adapter-facade.md)

## Template Method

Patrón de comportamiento en el que una clase base define el esqueleto de un algoritmo y las subclases rellenan algunos pasos sin cambiar su orden. Se apoya en la herencia y en el principio de Hollywood.

Ver también: [módulo 16](teoria/16-strategy-state-template-method.md)

## Test double

Objeto falso y simple (en memoria, que registra lo que recibe) que reemplaza a una dependencia real durante una prueba: un repositorio en memoria, un notificador falso.

Ver también: [módulo 06](teoria/06-dip.md)

## Thread-safe

Código que se comporta bien cuando varios hilos lo ejecutan a la vez (por ejemplo, que no crea dos instancias de un Singleton ni corrompe datos compartidos).

Ver también: [módulo 07](teoria/07-singleton.md)

## UML

Lenguaje gráfico estándar para dibujar la estructura y el comportamiento del software. En el curso se escribe con Mermaid.

Ver también: [módulo 00](teoria/00-introduccion.md)

## Wrapper

Objeto que envuelve a otro y le presenta una interfaz o comportamiento distinto, delegando en él. Adapter, Decorator y Proxy son tipos de wrapper.

Ver también: [módulo 12](teoria/12-adapter-facade.md)

## YAGNI

*You Aren't Gonna Need It*: no implementar funcionalidad hasta que se necesite de verdad, porque lo construido "por si acaso" suele sobrar.

Ver también: [módulo 01](teoria/01-buenas-practicas.md)
