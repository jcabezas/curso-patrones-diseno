# Preguntas de entrevista

> Archivo generado por `scripts/consolidar_preguntas.py`. No editar a mano: edita la sección de preguntas del módulo.


## Introducción y buenas prácticas


### Introducción y repaso de OOP ([módulo 00](teoria/00-introduccion.md))

**P1. ¿Qué es un patrón de diseño y qué no es?**
Es una solución reutilizable y con nombre a un problema de diseño que se repite, descrita como una estructura de clases y una explicación de cuándo aplicarla. No es código para copiar y pegar, ni una librería, ni un objetivo en sí mismo: se adapta a cada caso y solo se usa cuando el problema existe de verdad.

**P2. Herencia vs composición: ¿cuál prefieres y por qué?**
Prefiero composición. La herencia ata al hijo con el padre, y un cambio en el padre puede romper a todos los hijos; además, solo permite una jerarquía fija. Con composición el objeto delega en otros que puedes reemplazar, incluso en tiempo de ejecución. Uso herencia solo cuando hay una relación "es un" estable y real.

**P3. ¿Interfaz o clase abstracta?**
La interfaz define solo un contrato, sin estado ni código, y una clase puede cumplir varias. La clase abstracta puede traer estado y comportamiento compartido, pero solo se hereda una. Uso interfaz por defecto para separar contratos; elijo clase abstracta cuando varias subclases comparten código real que no quiero repetir.

**P4. ¿Qué es el polimorfismo y qué ventaja da?**
Es que el mismo mensaje produzca comportamientos distintos según el objeto que lo recibe. Por ejemplo, `cobrar` llama a `pagar` sin saber si el método es tarjeta o transferencia. La ventaja es que agregas comportamientos nuevos sin modificar el código que los usa, y eso reduce los `if` y facilita las pruebas.


### Buenas prácticas de desarrollo ([módulo 01](teoria/01-buenas-practicas.md))

**P1. ¿DRY significa nunca repetir código?**
No. DRY dice que cada pieza de *conocimiento* (una regla de negocio, una fórmula) debe vivir en un solo lugar. Dos trozos de código parecidos que cambian por razones distintas son duplicación accidental, y unirlos crea un acoplamiento falso. Me apoyo en la regla de tres: abstraigo cuando veo la tercera copia y sé que cambian juntas.

**P2. ¿Cuál es la diferencia entre KISS y YAGNI?**
KISS trata de *cómo* resuelves algo: elegir el diseño más simple que funcione. YAGNI trata de *qué* construyes: no implementar nada que nadie haya pedido todavía. Se complementan: con YAGNI haces menos cosas y con KISS haces cada una de la forma más sencilla. Ninguna significa descuidar la calidad del código.

**P3. ¿Qué dice la ley de Demeter y qué problema evita?**
Dice que un objeto solo debe hablar con sus vecinos directos, no con los objetos de sus vecinos: `pedido.region_despacho()` en lugar de `pedido.cliente.direccion.comuna.region`. Evita que quien llama conozca la estructura interna, de modo que si esa estructura cambia, solo se edita un lugar y no veinte. Reduce el acoplamiento.

**P4. Excepciones vs error como valor: ¿cuándo uso cada uno?**
Las excepciones (Python, TypeScript, PHP) mantienen limpio el camino feliz y suben hasta quien sabe qué hacer, pero el flujo de error queda invisible. El error como valor (Go) obliga a revisar cada llamada y deja explícito dónde se puede fallar, a costa de más código repetitivo. Uso cada uno según el lenguaje y reservo ambos para situaciones realmente excepcionales, no para resultados esperados como "no encontrado".

**P5. Nombra tres code smells y cómo los corriges.**
Long method: lo divido en funciones con nombre propio, una por paso. Magic number: lo reemplazo por una constante con nombre, como `IVA_PORCENTAJE`. Feature envy: si un método usa más datos de otro objeto que del propio, lo muevo a ese objeto. Un smell no es un error; es una señal para revisar.

**P6. ¿Cómo decides cuándo una función es demasiado larga?**
No cuento líneas; miro si hace más de una cosa o mezcla niveles de abstracción, por ejemplo validar, calcular y formatear juntos. Una prueba útil: si no puedo darle un nombre que describa todo lo que hace sin usar "y", hay que dividirla. También si necesito comentarios para separar secciones dentro de ella.


## Principios SOLID


### SRP: Responsabilidad única ([módulo 02](teoria/02-srp.md))

**P1. ¿Qué significa "razón para cambiar"?**
Es el motivo de negocio por el que habría que editar una clase, normalmente asociado a un área o persona que lo pide: Finanzas pide otro IVA, Contabilidad otro formato de factura, el equipo de datos otro motor de base de datos. Una clase cumple SRP cuando todos los cambios que la afectan vienen de un mismo origen. Si dos áreas distintas pueden pedir cambios sobre la misma clase, tiene dos responsabilidades.

**P2. ¿SRP es "una clase hace una sola cosa"?**
No, esa es una lectura común pero imprecisa. "Hacer una sola cosa" depende de qué tan vago sea el nombre: casi cualquier clase puede describirse como una cosa. El criterio correcto es que tenga una sola razón para cambiar. Una clase puede tener varios métodos y seguir cumpliendo SRP si todos cambian juntos y por la misma causa.

**P3. ¿Cómo detectas una violación de SRP en código existente?**
Busco señales concretas: la clase se importa desde muchos módulos sin relación, para probarla hay que mockear media aplicación, mezcla niveles (SQL, reglas de negocio y formato de salida) y los commits que la tocan hablan de motivos distintos. También miro su historial: si cambia con cada tarea del equipo, probablemente junta varias razones. El remedio es separar cada razón de cambio en su propia pieza y orquestarlas desde un servicio.

**P4. ¿Cuándo dividir es demasiado?**
Cuando separas cosas que cambian siempre juntas y terminas con muchas clases de un método que se llaman en cadena, y para seguir un flujo simple hay que abrir diez archivos. Una responsabilidad no es un método sino una razón de cambio. Divido cuando ya existen razones de cambio distintas o es muy probable que aparezcan, y no antes, por la misma lógica de YAGNI.


### OCP: Abierto/Cerrado ([módulo 03](teoria/03-ocp.md))

**P1. ¿Cómo se rompe OCP con un `switch`?**
Un `switch` (o una cadena de `if/elif`) sobre el tipo de algo obliga a editar esa función cada vez que aparece un caso nuevo, y suele estar copiado en varios lugares, así que hay que acordarse de todos. Cada edición arriesga romper los casos que ya funcionaban y obliga a probarlos de nuevo. La salida es reemplazar el `switch` por una interfaz con una implementación por caso y dejar que el polimorfismo elija.

**P2. ¿"Cerrado para modificación" es absoluto?**
No. No existe código cerrado contra todo cambio: si cambia el contrato de la interfaz (por ejemplo, `pagar` necesita un parámetro nuevo), hay que modificar el código existente. El cierre es estratégico: se protege contra los tipos de cambio más probables, como agregar un método de pago, y se acepta modificar para los demás. Además, corregir un bug sí es una modificación legítima; el principio habla de agregar comportamiento.

**P3. ¿Qué patrones sirven para cumplir OCP?**
Strategy permite intercambiar algoritmos detrás de una interfaz (envío, descuentos), Factory Method delega qué clase concreta crear a una subclase o función, y Decorator agrega comportamiento envolviendo un objeto sin editar su clase. También Observer (nuevos suscriptores sin tocar al emisor) y Template Method (variar pasos sin tocar el esqueleto) siguen la misma lógica. Todos comparten la receta: depender de una abstracción y agregar variaciones como código nuevo.

**P4. ¿Cuándo NO aplicarlo?**
Cuando solo hay un caso o dos ramas que probablemente no cambiarán: la abstracción es costo sin beneficio y, al adivinar mal, queda con una forma equivocada que luego hay que desarmar. Por YAGNI conviene esperar al segundo o tercer caso real, y recién ahí extraer la interfaz. Aplica OCP donde ya viste que el sistema cambia, y no en cada `if` del código.


### LSP: Sustitución de Liskov ([módulo 04](teoria/04-lsp.md))

**P1. Enuncia LSP con tus palabras.**
Si un código funciona con una clase base, tiene que seguir funcionando igual cuando le pasas cualquiera de sus subclases, sin saber cuál es. La subclase debe respetar lo que la base promete: aceptar lo mismo, garantizar al menos lo mismo y mantener sus invariantes. No basta con que los tipos encajen: tiene que comportarse como la base.

**P2. ¿Cuáles son las señales de una violación de LSP?**
Subclases que lanzan `NotImplementedError` o `UnsupportedOperationException` en un método heredado, métodos que se dejan vacíos o devuelven un valor falso, y clientes que hacen `isinstance` o `switch` por tipo antes de llamar. También que la subclase valide más (endurezca una precondición) o devuelva algo que la base nunca devolvería (debilite una poscondición). Cuando el cliente necesita saber qué subclase tiene, la sustitución ya falló.

**P3. ¿Qué tiene que ver LSP con el diseño por contrato?**
LSP es diseño por contrato aplicado a la herencia. Cada método tiene precondiciones (lo que exige), poscondiciones (lo que garantiza) e invariantes de clase (lo que siempre se cumple). Una subclase sustituible puede relajar las precondiciones y reforzar las poscondiciones, pero nunca lo contrario, y debe conservar los invariantes.

**P4. ¿LSP se cumple solo con que el código compile?**
No. El compilador verifica firmas (nombres y tipos), no comportamiento: `DescuentoVIP` devuelve un `int` y compila, pero deja totales negativos y rompe la poscondición. En lenguajes con interfaces implícitas, como Go, pasa igual: un tipo con el método correcto satisface la interfaz sin garantizar su contrato. Por eso LSP se protege documentando el contrato, con pruebas que ejecuten el mismo caso contra todas las implementaciones y, cuando se puede, con jerarquías más pequeñas.


### ISP: Segregación de interfaces ([módulo 05](teoria/05-isp.md))

**P1. ¿En qué se diferencia ISP de SRP?**
SRP mira a la **implementación**: una clase debe tener una sola razón para cambiar. ISP mira a la **interfaz desde el punto de vista del cliente**: nadie debe depender de métodos que no usa. Se parecen porque ambos separan, pero se pueden violar por separado: una clase puede tener una sola responsabilidad y aun así exponer una interfaz gorda que obliga a sus clientes a conocer métodos que no necesitan.

**P2. ¿Qué síntoma delata una interfaz gorda?**
Implementaciones que lanzan `NotImplementedError` o devuelven valores falsos en métodos que no les corresponden, clientes que usan una fracción pequeña de la interfaz, y cambios en la interfaz que obligan a tocar clases y mocks sin relación con ese cambio. Un indicador práctico: si para escribir un mock de prueba tienes que implementar diez métodos y el cliente usa dos, la interfaz es demasiado grande.

**P3. ¿Cómo se relaciona ISP con LSP?**
Una interfaz gorda empuja a las implementaciones a negarse a cumplir parte de ella, por ejemplo lanzando `NotImplementedError`, y eso es justo una violación de LSP: la subclase no puede sustituir a la base ([módulo 04](teoria/04-lsp.md)). Segregar la interfaz ataca la causa: cada implementación solo promete lo que puede cumplir, y por eso suele resolver también el problema de sustitución.

**P4. ¿Aplica ISP en lenguajes sin interfaces formales, como Python?**
Sí, porque el principio trata de dependencias y no de la palabra `interface`. Python usa **duck typing** (un objeto sirve si tiene los métodos que se le piden, sin importar su clase; [glosario](glosario.md#duck-typing)): el cliente depende de hecho solo de los métodos que invoca. Aun así, ISP importa: una clase base abstracta gorda sigue obligando a implementar todo, y los tipos poco claros esconden qué usa cada cliente. Con `typing.Protocol` se declara explícitamente el conjunto mínimo de métodos que cada función necesita, y un verificador como mypy lo comprueba.


### DIP: Inversión de dependencias ([módulo 06](teoria/06-dip.md))

**P1. ¿En qué se diferencian DIP, inyección de dependencias e IoC?**
DIP es el principio: el código de alto nivel debe depender de abstracciones, no de detalles concretos. La inyección de dependencias es una técnica para lograrlo: la clase recibe sus dependencias desde afuera, normalmente por constructor, en lugar de crearlas. IoC es el concepto más amplio de ceder a un marco o contenedor el control de crear y conectar objetos, y un contenedor de IoC es una herramienta que automatiza la inyección; se puede cumplir DIP con inyección manual y sin ningún contenedor.

**P2. ¿Por qué se dice "invertir"?**
En el diseño ingenuo, las dependencias del código fuente siguen el flujo de llamadas: la regla de negocio importa y construye al detalle técnico, así que apunta "hacia abajo". Con DIP la regla define la interfaz que necesita y el detalle la implementa, de modo que la dependencia del código fuente del detalle apunta hacia la regla. El flujo de ejecución sigue yendo de la regla al detalle, pero las flechas de dependencia se invierten, y por eso un cambio en el detalle ya no obliga a tocar la regla.

**P3. ¿Cómo facilita DIP las pruebas?**
Como la clase recibe sus dependencias por la interfaz, en una prueba se le pasan dobles de prueba: un repositorio en memoria en lugar de la base de datos y un notificador falso que guarda los mensajes en una lista en lugar de enviar correos. La prueba es rápida, determinista y no necesita infraestructura, y además puede inspeccionar qué pasó (qué se guardó, qué se envió) y simular fallos como un pago rechazado. Sin DIP, para probar la misma regla haría falta una base y un servidor de correo reales o parchear imports.

**P4. ¿Usar una interfaz es lo mismo que aplicar DIP?**
No, es necesario pero no suficiente. Si la clase sigue haciendo `new` de la implementación concreta en su constructor, aunque declare el campo con tipo de interfaz, sigue atada a ella. Además, la abstracción debe expresar lo que necesita el cliente y no los detalles del proveedor: una interfaz `ClienteMySQL` con `ejecutar_sql(consulta)` está copiada del detalle y no desacopla nada, mientras que `PedidoRepository` con `guardar` y `obtener` pertenece al dominio. DIP se cumple cuando la regla define el contrato, el detalle lo implementa y alguien externo (el composition root) conecta ambos.


## Patrones creacionales


### Creacionales: Singleton ([módulo 07](teoria/07-singleton.md))

**P1. ¿Cómo haces thread-safe un Singleton?**
Hay que evitar que dos hilos creen la instancia a la vez. Las opciones son crearla al cargar la clase o el módulo (inicialización temprana, segura porque el cargador del lenguaje lo hace una sola vez), proteger la creación con un candado y doble comprobación (Python), o usar una primitiva del lenguaje como `sync.Once` en Go. Además, si el objeto es mutable, la instancia única no basta: hay que sincronizar también el acceso a su estado, o mejor hacerlo inmutable.

**P2. ¿Por qué muchos lo consideran un antipatrón?**
Porque es estado global disfrazado. Las clases que lo usan esconden esa dependencia (no aparece en su constructor ni en su firma), quedan acopladas a una clase concreta, y las pruebas se contaminan entre sí porque el estado persiste. Además mezcla dos responsabilidades en una clase, su lógica y el control de su propia creación, lo que viola SRP. El problema no es tener una instancia, sino imponerla desde la clase con acceso global.

**P3. ¿Qué alternativas hay al Singleton?**
La principal es crear una sola instancia en el composition root e inyectarla por constructor: se mantiene la unicidad sin el acceso global, y la dependencia es explícita y reemplazable (DIP). Otras son el módulo como singleton en Python y TypeScript (una constante exportada) o un contenedor de dependencias que registre el servicio con vida única. En los tres casos se conserva la ventaja (un único objeto) y se evita la desventaja (estado global).

**P4. ¿En qué se diferencia un Singleton de una variable global?**
Las dos son accesibles desde cualquier parte, pero el Singleton agrega dos garantías: solo puede existir una instancia (el constructor es privado) y se crea de forma perezosa, cuando se pide por primera vez, en lugar de existir desde el arranque. A cambio hereda los mismos defectos del estado global: dependencias ocultas y pruebas difíciles. Es una variable global más ordenada, pero no elimina el acoplamiento.


### Creacionales: Factory Method ([módulo 08](teoria/08-factory-method.md))

**P1. ¿En qué se diferencian Factory Method, Simple Factory y Abstract Factory?**
Simple Factory es una función o clase que construye objetos según un parámetro; no es un patrón GoF. Factory Method es un método de una clase base que las subclases sobrescriben para decidir qué producto crear. Abstract Factory es una interfaz que crea familias de productos relacionados que deben usarse juntos, no uno solo.

**P2. ¿Qué problema resuelve Factory Method?**
Evita que el código cliente cree clases concretas con `new` y repita cadenas de `if` por tipo. La decisión de qué clase instanciar queda en un solo lugar, y quien usa el objeto trabaja contra una interfaz. Así, un tipo nuevo no obliga a modificar todos los puntos donde se usa.

**P3. ¿Cómo se relaciona con OCP?**
Sin el patrón, cada tipo nuevo exige editar las cadenas de `if` repartidas por el código, es decir, modificar código existente. Con él, se extiende agregando una clase de producto y su creador (o una entrada en la tabla de la fábrica), y el código que usa el producto no se toca. También apoya DIP, porque el cliente depende de la interfaz y no de la clase concreta.

**P4. ¿Cómo se ve Factory Method en Go?**
Go no tiene herencia, así que no hay creador abstracto con subclases. El patrón se reduce a una función constructora que devuelve una interfaz, como `NuevoNotificador(canal string) (Notificador, error)`. Para variar la creación se inyecta la función como valor (`func() Notificador`).

**P5. ¿Por qué no usar `new` directamente?**
Porque acopla el código a una clase concreta: cambiarla, reemplazarla por un doble en las pruebas o agregar una variante obliga a editar cada lugar donde aparece. Con una fábrica, ese conocimiento está en un solo punto. Aun así, si hay un único tipo y no se espera otro, `new` directo es más simple y correcto.


### Creacionales: Abstract Factory ([módulo 09](teoria/09-abstract-factory.md))

**P1. ¿En qué se diferencia Abstract Factory de Factory Method?**
Factory Method crea un solo tipo de producto mediante un método que las subclases sobrescriben. Abstract Factory es un objeto con varios métodos de creación que produce una familia completa de productos que deben usarse juntos. La diferencia clave es que la segunda garantiza la compatibilidad entre las piezas.

**P2. ¿Cuándo elegir uno u otro?**
Si necesitas variar un solo objeto según el contexto (el canal de notificación), usa Factory Method o una función creadora. Si necesitas variar varios objetos a la vez y deben ser coherentes entre sí (pago, antifraude y documento de una región), usa Abstract Factory. Si hay una sola familia, ninguno de los dos hace falta.

**P3. ¿Qué principio se resiente al agregar un producto nuevo a la familia?**
OCP. Agregar `crearCalculadorImpuestos()` obliga a modificar la interfaz de la fábrica y todas sus implementaciones, así que el diseño no está cerrado a ese tipo de extensión. En cambio, agregar una familia nueva no toca código existente. Por eso conviene usarlo cuando las familias cambian más que los tipos de producto.

**P4. ¿Qué ventaja da frente al `if region` repartido por el código?**
Concentra en un solo punto la decisión de qué familia se usa, y el cliente trabaja contra interfaces (DIP). Además impide por construcción combinaciones inválidas, como Webpay con invoice, que con `if` sueltos dependen de que nadie se equivoque. Agregar una región es escribir una fábrica nueva.

**P5. ¿Un ejemplo real?**
Un toolkit de interfaz gráfica multiplataforma: una fábrica por sistema operativo que crea botones, menús y ventanas con el mismo aspecto. Otro: las bibliotecas de acceso a bases de datos, donde cada driver (PostgreSQL, MySQL) entrega su propia conexión, comando y lector de resultados, que solo funcionan entre sí.

**P6. ¿Cómo se ve en Go?**
Una interfaz con varios métodos de creación y un `struct` por familia que la satisface de forma implícita, sin herencia. Quien la usa recibe la interfaz y no sabe qué familia hay detrás.


### Creacionales: Builder ([módulo 10](teoria/10-builder.md))

**P1. ¿En qué se diferencia Builder de Factory?**
Una fábrica decide **qué clase** instanciar y devuelve el objeto en una sola llamada. Builder se ocupa de **cómo se arma** un objeto complejo: acumula datos en varios pasos y entrega el resultado al final, validado. Las fábricas varían el tipo; Builder maneja la complejidad de la construcción.

**P2. ¿Qué es el constructor telescópico y por qué es un problema?**
Es un constructor (o una cadena de constructores sobrecargados) con una fila de parámetros opcionales que crece con cada opción nueva. Los llamados se vuelven ilegibles, es fácil pasar un valor en la posición equivocada sin que el compilador lo note si los tipos coinciden, y no hay dónde validar el conjunto. Builder lo reemplaza con pasos con nombre.

**P3. ¿Cómo se garantiza que el objeto final sea válido e inmutable?**
La validez se garantiza haciendo que `construir()` sea la única vía de crear el objeto y que ahí se revisen las reglas (cliente presente, al menos un item). La inmutabilidad se logra con un objeto sin setters (propiedades `readonly`, `frozen=True`, campos sin exportar) y copiando las colecciones que recibe, para que el builder no pueda alterarlas después.

**P4. ¿Cómo se hace en Go?**
Con *functional options*: la función constructora recibe los datos obligatorios como argumentos y las opciones como funciones variádicas (`NuevoPedido(cliente, ConCupon("X"), ConNota("..."))`). Aplica cada opción sobre el objeto, valida y devuelve `(Pedido, error)`. No hace falta un tipo builder, y agregar una opción es escribir una función.

**P5. ¿Para qué sirve el Director?**
Es un objeto o función que conoce recetas de construcción ("pedido de regalo exprés") y las ejecuta sobre un builder, de modo que no se repitan en cada llamador. Es opcional: si nadie repite una secuencia de pasos, no se necesita.


### Creacionales: Prototype ([módulo 11](teoria/11-prototype.md))

**P1. ¿Cuál es la diferencia entre copia superficial y copia profunda?**
La superficial duplica el objeto, pero sus campos de referencia (listas, diccionarios, otros objetos) siguen apuntando a los mismos objetos que el original. La profunda duplica también todo lo que el objeto contiene, recursivamente, así que el clon es totalmente independiente. Con la superficial, modificar la lista del clon modifica la del original.

**P2. ¿Cuándo usarías Prototype en vez de un constructor?**
Cuando construir el objeto es costoso o requiere mucha configuración, y es más barato partir de uno ya configurado y ajustarlo (repetir un pedido, una plantilla). También cuando el código que copia solo conoce una interfaz y no la clase concreta, de modo que un tipo nuevo no obliga a modificarlo (OCP). Si el objeto es simple o inmutable, un constructor o compartir la instancia es mejor.

**P3. ¿Cómo evitas el bug de la lista compartida al clonar?**
Haciendo que `clonar()` realice una copia profunda: `copy.deepcopy` en Python, `structuredClone` en TypeScript, un `__clone` que clone cada objeto interno en PHP, o copiar la slice a mano en Go. Además conviene un test que clone, modifique el clon y compruebe que el original no cambió. Una alternativa es usar objetos inmutables, donde compartir no es un riesgo.

**P4. ¿Cómo se hace en Go?**
Go no tiene `clone` automático: asignar un struct copia solo el nivel superficial, y las slices y maps quedan compartidos. Se escribe un método `Clonar()` que copia explícitamente cada slice con `append([]ItemCarrito(nil), p.Items...)` o `slices.Clone`, y los maps con un bucle. Con un receptor por valor, el struct ya llega copiado y solo hay que reemplazar los campos que contienen referencias.


## Patrones estructurales


### Estructurales: Adapter y Facade ([módulo 12](teoria/12-adapter-facade.md))

**P1. ¿Cuál es la diferencia entre Adapter y Facade?**
Adapter se centra en la **compatibilidad**: traduce la interfaz de un objeto a la que el cliente ya esperaba, normalmente envolviendo uno solo. Facade se centra en la **simplicidad**: crea una interfaz nueva y más pequeña sobre varios objetos de un subsistema. En el adapter la interfaz de destino ya existe; en la fachada la diseñas tú.

**P2. ¿En qué se diferencia Adapter de Decorator?**
Ambos envuelven un objeto, pero con fines distintos. El adapter **cambia** la interfaz para que encaje, porque el objeto adaptado no era compatible. El decorator **mantiene** la interfaz y añade comportamiento (logs, reintentos), de modo que se pueden apilar; Decorator se verá en el siguiente módulo.

**P3. ¿Qué es un Adapter de objeto y qué uno de clase?**
El de **objeto** usa composición: el adapter contiene una instancia del adaptado y delega; es la forma de este módulo y funciona en todos los lenguajes. El de **clase** usa herencia múltiple: el adapter hereda a la vez de la interfaz esperada y de la clase adaptada, lo que solo es posible en lenguajes como C++ o Python y lo acopla a una clase concreta. Por eso, y por preferir composición sobre herencia, casi siempre se usa el de objeto.

**P4. ¿Facade viola la Ley de Demeter o la refuerza?**
La refuerza. La [Ley de Demeter](glosario.md#ley-de-demeter) (hablar solo con los vecinos inmediatos) dice que el cliente no debería conocer ni recorrer los objetos internos de un subsistema. La fachada es ese único vecino: el cliente le habla a ella y ella conoce a los demás. Eso sí, la fachada conoce a todos los subsistemas, así que debe limitarse a coordinar.

**P5. Da un ejemplo real de cada uno.**
Adapter: envolver el SDK de un proveedor de pagos o de correo detrás de la interfaz propia del sistema (`MetodoPago`, `Notificador`), para cambiar de proveedor sin tocar el negocio. Facade: un `CheckoutFacade` que orquesta stock, pago, envío y aviso; o la API de alto nivel de una librería como `requests` de Python, que oculta sockets, HTTP y TLS. En ambos casos el resto del código depende de algo estable y simple.


### Estructurales: Decorator y Proxy ([módulo 13](teoria/13-decorator-proxy.md))

**P1. ¿Cuál es la diferencia entre Decorator y Proxy, si ambos tienen la misma interfaz?**
La intención. Decorator **agrega** comportamiento al objeto y está pensado para apilarse: el cliente compone las capas que quiere. Proxy **controla el acceso** al objeto (caché, permisos, carga diferida) y suele ser él quien conoce o crea al sujeto real, de modo que el cliente ni siquiera sabe que existe. La estructura es casi idéntica; la pregunta correcta es "¿qué quiero lograr?".

**P2. ¿Por qué Decorator es mejor que la herencia para combinar comportamientos?**
La herencia fija las combinaciones al compilar y obliga a una subclase por combinación: con tres opciones hay ocho clases y cada una nueva las duplica. Con Decorator cada comportamiento es una clase y la combinación se arma en tiempo de ejecución, en el orden que se necesite. El costo es que hay más objetos pequeños y el orden de las capas importa (IVA antes o después del cupón da 24750 o 23800).

**P3. ¿Qué tipos de proxy existen?**
El **virtual** crea un objeto caro solo cuando se usa por primera vez (*lazy loading*). El de **protección** comprueba permisos antes de delegar. El **remoto** representa localmente a un objeto que vive en otro proceso o máquina y oculta la comunicación (como un cliente de un servicio). El de **caché** guarda resultados para no repetir trabajo, como `CatalogoProxyCache`. Todos comparten la misma interfaz que el objeto real.

**P4. ¿En qué se parece Decorator a un middleware?**
Un middleware es un decorador de una función de manejo de peticiones: recibe el siguiente manejador, hace algo antes y después (autenticar, registrar, medir tiempo) y delega. Se apilan en un orden, igual que `ConIVA(ConCupon(...))`, y el orden cambia el resultado. En Go es literalmente `func(http.Handler) http.Handler`, una función que envuelve a otra.

**P5. ¿Por qué el decorador o el proxy deben tener la misma interfaz que el objeto envuelto?**
Para que el cliente no note la diferencia: puede recibir el objeto real, un proxy o una pila de decoradores sin cambiar una línea (DIP), y además los decoradores se pueden apilar porque cada uno acepta cualquier otro como interno. Es sustituibilidad pura: el envoltorio debe respetar el contrato del original ([LSP](teoria/04-lsp.md)). Si la interfaz cambiara, sería un Adapter.


### Estructurales: Composite y Flyweight ([módulo 14](teoria/14-composite-flyweight.md))

**P1. ¿Para qué sirve el patrón Composite?**
Para tratar de la misma forma a un objeto individual y a un grupo de objetos cuando el dominio forma un árbol. Hoja y compuesto implementan la misma interfaz (`ComponenteCatalogo.precio()`), y el compuesto delega en sus hijos de forma recursiva. El cliente deja de escribir `if es_combo` y recorridos repetidos, y los combos pueden anidarse a cualquier profundidad.

**P2. ¿En qué se diferencia Composite de Decorator, si ambos son recursivos?**
Decorator envuelve un único objeto para agregarle comportamiento, y el resultado sigue siendo "ese objeto, con algo más". Composite contiene muchos hijos y combina sus resultados (suma, recorrido, conteo): modela una estructura parte-todo, no una extensión. En el código la estructura se parece; la pista es si el nodo tiene una lista de hijos o un solo interno.

**P3. ¿Qué es el estado intrínseco y qué es el extrínseco en Flyweight?**
El intrínseco es lo que no depende del contexto y es igual para muchos objetos (descripción e imagen del tipo de producto); es inmutable y vive en el flyweight compartido. El extrínseco depende de cada uso (SKU y precio de un ítem): lo guarda el contexto o se pasa como argumento (`mostrar(sku, precio)`). La técnica consiste en mover al flyweight lo primero y dejar fuera lo segundo.

**P4. ¿Cuándo NO conviene usar Flyweight?**
Cuando hay pocos objetos, cuando casi todo su estado es distinto entre ellos o cuando el estado que se querría compartir es mutable. En esos casos el ahorro de memoria es mínimo y el costo es complejidad extra (fábrica, separación de estados, sincronización en lenguajes concurrentes como Go). Es una optimización: se aplica después de medir (YAGNI), no al diseñar.

**P5. ¿Cuál es la diferencia entre Flyweight y una caché?**
Una caché busca ahorrar cómputo o E/S: guarda **resultados** costosos de obtener y puede expulsarlos (por TTL, tamaño máximo o LRU) cuando ya no convienen. Un Flyweight busca ahorrar memoria compartiendo estado intrínseco **inmutable** entre muchos objetos, y la fábrica lo retiene mientras ella viva (normalmente toda la ejecución); no lo expulsa. La fábrica se parece a una caché por clave, pero lo que la distingue es la intención (memoria frente a tiempo) y que lo compartido es inmutable.


### Estructurales: Bridge ([módulo 15](teoria/15-bridge.md))

**P1. ¿En qué se diferencia Bridge de Adapter?**
Ambos usan composición, pero con intención opuesta. Adapter se aplica después, para hacer compatible una clase existente con la interfaz que el cliente espera. Bridge se planifica de antemano para separar una abstracción de su implementación y que las dos evolucionen por separado.

**P2. ¿En qué se diferencia Bridge de Strategy?**
El código se parece, porque en ambos un objeto delega en otro mediante una interfaz. En Strategy el cliente elige un algoritmo intercambiable y no hay una jerarquía de abstracciones del lado que delega. En Bridge hay dos jerarquías que crecen: la de la abstracción (`Aviso`, con `AvisoPedido` y `AvisoPromocion`) y la del implementor (`Canal`, con `CanalEmail` y `CanalSMS`).

**P3. ¿Qué es la explosión de subclases?**
Es cuando una clase varía en dos dimensiones y se resuelve con herencia: hay una subclase por cada combinación. Con 2 tipos de aviso y 3 canales son 6 clases; con 3 tipos y 4 canales, 12. Con Bridge el número es la suma (3 + 4 = 7), no el producto.

**P4. ¿Cómo se nota que necesitas Bridge?**
Cuando los nombres de las clases combinan dos ideas (`AvisoPedidoSMS`, `ReportePDFVentas`) y cada característica nueva obliga a crear varias clases a la vez. Otra señal es el texto o la lógica repetida en varias subclases que solo se diferencian en el "cómo". Entonces conviene separar las dos dimensiones y componerlas.

**P5. ¿Cómo se ve Bridge en Go?**
Son dos interfaces y una composición por campo: `AvisoPedido` guarda un `Canal` y le delega. Como Go no tiene herencia, no hay jerarquía de subclases que explote; el patrón es simplemente la forma natural de armar el programa.


## Patrones de comportamiento


### De comportamiento: Strategy, State y Template Method ([módulo 16](teoria/16-strategy-state-template-method.md))

**P1. ¿Cuál es la diferencia entre Strategy y State, si ambos delegan en un objeto con la misma interfaz?**
Quién cambia el objeto y por qué. En Strategy el cliente elige el algoritmo desde fuera y las estrategias no se conocen entre sí; son alternativas intercambiables para el mismo trabajo (`EnvioExpress` o `RetiroEnTienda`). En State el propio contexto cambia de estado como consecuencia de sus operaciones, y cada estado conoce a sus sucesores (`Pagado` devuelve `Enviado`). La estructura es casi idéntica; la intención no.

**P2. ¿En qué se diferencia Strategy de Template Method?**
Ambos permiten variar un algoritmo, pero Strategy lo hace por composición y Template Method por herencia. Con Strategy se reemplaza el algoritmo completo y se puede cambiar en tiempo de ejecución; con Template Method el esqueleto queda fijo en la clase base y las subclases solo rellenan algunos pasos, y la elección se hace al crear el objeto. Si solo cambia un paso dentro de un flujo común, usa Template Method; si cambia todo el método, Strategy.

**P3. ¿Cuándo usarías State en vez de un enum con un switch?**
El enum con `switch` basta cuando hay pocos estados y una sola operación que depende de ellos. State compensa cuando varias operaciones (`pagar`, `enviar`, `cancelar`) cambian según el estado: el `switch` se copiaría en cada una y un estado nuevo obligaría a editarlas todas. Con State cada estado concentra sus reglas en una clase, las transiciones inválidas fallan por defecto y agregar un estado es agregar una clase (OCP).

**P4. ¿Template Method contradice "composición sobre herencia"?**
Usa herencia, así que sí está en tensión con esa guía, pero es un uso razonable cuando el esqueleto es estable, la jerarquía es poco profunda y las subclases solo rellenan pasos. Sus costos son que la subclase queda acoplada a la base (clase base frágil) y que el comportamiento no se puede cambiar en ejecución. Si esos costos pesan, se pasa el paso variable como un objeto o una función (un Strategy): es lo que se hace en Go, que no tiene herencia.

**P5. ¿Cómo se ve Strategy en Go?**
Si la interfaz tiene un solo método, la estrategia es simplemente una función: `type CostoEnvio func(Pedido) int`, y cualquier función con esa firma (incluida una anónima) sirve. Así funcionan `sort.Slice` con su función de comparación y `http.HandlerFunc`. Se usa una interfaz cuando la estrategia necesita varios métodos (como `Nombre()` y `Costo()`) o guarda estado.

**P6. ¿Qué es el principio de Hollywood?**
Es la regla "no nos llames, te llamamos": el código de alto nivel controla el flujo y llama al de bajo nivel, y no al revés. En Template Method, la clase base llama a `leer()` y a los demás pasos; la subclase no decide cuándo se ejecutan. Es una forma de inversión de control, la misma idea de fondo que el DIP y la que tienen los frameworks (`setUp` de las pruebas, los *hooks* de ciclo de vida).


### De comportamiento: Observer, Mediator y Chain of Responsibility ([módulo 17](teoria/17-observer-mediator-chain.md))

**P1. ¿Cuál es la diferencia entre Observer y Pub/Sub?**
En Observer el sujeto conoce a sus observadores (mantiene la lista) y los llama directamente, normalmente en el mismo proceso y de forma síncrona. En Pub/Sub hay un intermediario, el *broker* o bus de mensajes, que desacopla del todo a publicadores y suscriptores: no se conocen, se comunican por temas y la entrega puede ser asíncrona, persistente y entre procesos (Kafka, Redis, RabbitMQ). `BusEventos` está en el medio: un Pub/Sub en proceso, síncrono y sin garantías de entrega.

**P2. ¿En qué se diferencian Observer y Mediator?**
Ambos desacoplan objetos, pero Observer es de uno a muchos y sin coordinación: el publicador avisa y cada suscriptor decide qué hace. Mediator centraliza en un objeto las reglas sobre quién debe reaccionar a qué, así que los colegas solo lo conocen a él. Observer facilita agregar suscriptores; Mediator facilita ver y cambiar las reglas de coordinación, a costa de poder convertirse en un God Object.

**P3. ¿Cómo evitas las fugas de memoria con observers?**
La fuga ocurre porque el sujeto guarda una referencia fuerte a cada observador: si un objeto de vida corta (una pantalla, una sesión) se suscribe y nunca se da de baja, no se libera. Se evita llamando a `desuscribir` (o a la función de baja que devuelve `suscribir`) cuando el suscriptor deja de existir, o usando referencias débiles (`weakref` en Python, `WeakRef` en JavaScript). En Go la variante es la goroutine que sigue leyendo un canal que nadie cierra.

**P4. ¿Qué diferencia hay entre Chain of Responsibility y Decorator?**
Estructuralmente son parecidos: objetos que envuelven a otro y delegan. Un Decorator siempre delega en el objeto envuelto y agrega algo antes o después; en una cadena cada eslabón decide si procesa la solicitud, la pasa o la corta devolviendo sin llamar al siguiente. Por eso la cadena modela "quién se encarga" o "pasa todas las reglas", y el Decorator modela "agrégale esto".

**P5. ¿Cuándo un mediador es un mal olor?**
Cuando se convierte en un God Object: acumula todas las reglas de la pantalla o del sistema, crece a cientos de líneas con un `if` por cada evento y todo cambio pasa por él. Entonces solo has movido el desorden de muchos objetos a uno. También es mal olor si media entre dos objetos solamente (una referencia directa bastaba) o si los colegas empiezan a tener reglas de negocio y el mediador solo reenvía. La salida es dividirlo por flujo o usar eventos.

**P6. ¿Dónde ves estos patrones en software real?**
Observer está en los eventos del DOM (`addEventListener` suscribe un callback y `removeEventListener` da de baja) y en los eventos de Node.js (`EventEmitter`). Chain of Responsibility es el middleware: Express, Koa, los `http.Handler` de Go o el pipeline de middleware de Laravel pasan la petición de un eslabón al siguiente y cualquiera puede cortarla con una respuesta. Mediator aparece en los controladores de pantallas de interfaz y en las torres de control de los frameworks de mensajería (el `MediatR` de .NET, por ejemplo).


### De comportamiento: Command, Memento e Iterator ([módulo 18](teoria/18-command-memento-iterator.md))

**P1. ¿Cómo implementas undo/redo?**
Con el patrón Command: cada acción es un objeto con `ejecutar()` y `deshacer()`, y un historial mantiene dos pilas. Ejecutar apila el comando en "hechos" y vacía "deshechos"; deshacer saca de "hechos", llama a `deshacer()` y lo apila en "deshechos"; rehacer hace lo inverso. Cada comando debe guardar lo que necesita para revertirse, como `QuitarDelCarrito`, que recuerda la línea quitada.

**P2. ¿En qué se diferencian Command y Strategy?**
Ambos convierten comportamiento en un objeto, pero con intención distinta. Strategy es un algoritmo intercambiable que el cliente elige y reutiliza (calcular el envío); Command es una acción concreta, con sus datos, que se crea, se guarda y puede deshacerse o encolarse. Un Strategy suele no tener estado ni deshacer; un Command casi siempre lleva los parámetros de la solicitud.

**P3. ¿Memento rompe el encapsulamiento?**
No, si está bien hecho: el memento es opaco y solo el originador sabe leer su contenido, así que el cuidador puede guardarlo pero no inspeccionarlo ni modificarlo. Rompería el encapsulamiento si el memento expusiera getters públicos para que otros lo lean. Cada lenguaje lo logra con sus mecanismos (convención en Python, módulo y `WeakMap` en TypeScript, campos no exportados en Go, un closure en PHP), y ninguno es infalible frente a quien quiera forzarlo.

**P4. ¿Qué diferencia hay entre un iterador interno y uno externo?**
En el externo el cliente controla el avance: pide "el siguiente" y decide cuándo parar, como `next()` en Python, `for...of` en TypeScript o `iter.Pull` en Go. En el interno la colección controla el bucle y llama a una función del cliente por cada elemento, como `forEach` o un `iter.Seq` de Go, donde el cuerpo del `for` es el callback. El externo es más flexible (puedes recorrer dos colecciones a la vez); el interno es más simple de escribir.

**P5. ¿Por qué los generadores simplifican Iterator?**
El Iterator clásico exige una clase iteradora con estado explícito (posición, página actual, si terminó) y un método `siguiente`. Un generador deja que el lenguaje guarde ese estado: el código se escribe como un bucle normal con `yield` y la ejecución se pausa entre elementos. Además son perezosos de forma natural: `CatalogoPaginado` pide una página solo cuando el cliente necesita el siguiente producto.

**P6. Dame un ejemplo real que combine estos patrones.**
Un editor de texto: cada edición (insertar, borrar) es un Command con `deshacer()`, lo que da el undo/redo con Ctrl+Z; guardar una versión completa del documento para volver a ella es un Memento; y recorrer sus líneas o los resultados de una búsqueda sin cargar todo el archivo es un Iterator. Una cola de trabajos es la misma idea de Command aplicada a tareas que se ejecutan después, con reintentos, y cuya lista de pendientes se recorre con un iterador.


### Comportamiento sobre estructuras: Visitor e Interpreter ([módulo 19](teoria/19-visitor-interpreter.md))

**P1. ¿Qué es el doble despacho y por qué lo usa Visitor?**
Es elegir el método según el tipo de dos objetos en vez de uno. Primero `elemento.aceptar(visitante)` despacha por el tipo del elemento; dentro, `visitante.visitarDigital(this)` despacha por el tipo del visitante con el tipo del elemento ya resuelto. Así se llega al método correcto sin `isinstance`, aunque la mayoría de los lenguajes solo despachan por el tipo del receptor.

**P2. ¿Cuándo elegirías Visitor y cuándo no?**
Lo elijo cuando la jerarquía de elementos es estable y las operaciones crecen (IVA, exportación, resumen), porque cada operación nueva es una clase sin tocar los elementos. No lo uso cuando cambian los tipos: agregar uno obliga a modificar la interfaz del visitante y todos los visitantes. Es el trade-off del OCP: se cumple para las operaciones, no para los tipos.

**P3. ¿En qué se diferencia Visitor de poner un método en cada clase (polimorfismo simple)?**
Con polimorfismo simple, agregar un tipo es fácil (una clase nueva) pero agregar una operación obliga a editar todas las clases y a mezclar responsabilidades en ellas. Visitor invierte el costo: agregar una operación es fácil y agregar un tipo es caro. La elección depende de qué eje crece más seguido.

**P4. ¿Para qué sirve Interpreter y cuándo es excesivo?**
Sirve para evaluar un lenguaje pequeño y estable representando cada regla de su gramática como una clase que forma un árbol, como las reglas de cupones con `Y`, `O` y comparaciones. Es excesivo si las reglas son pocas y no cambian (basta un `if`) o si la gramática es grande: el número de clases crece y hace falta un parser, para lo que se usan generadores como ANTLR.

**P5. ¿Qué relación hay entre Interpreter y Composite?**
El árbol sintáctico de un Interpreter es un Composite: los nodos terminales son las hojas (`Comparacion`) y los no terminales son los compuestos (`Y`, `O`), que delegan `interpretar` en sus hijos. La diferencia es la intención: Composite trata igual al todo y a la parte; Interpreter le da a cada nodo el significado de una regla de la gramática y evalúa la expresión completa.


## Antipatrones y cierre


### Módulo 20: Antipatrones y caso de cierre ([módulo 20](teoria/20-antipatrones-y-cierre.md))

**P1. ¿Cuál es el peor mal uso de patrones que has visto?**
El caso típico es el patrón aplicado "por si acaso": una `AbstractFactory` con una sola familia, o un Singleton para cada servicio, que esconde dependencias y hace imposible probar una clase sin las demás. El costo aparece meses después, cuando hay que recorrer cinco capas para cambiar una línea. Lo arreglo con el camino inverso: volver al código simple y volver a introducir el patrón solo donde el dolor es real.

**P2. ¿Cómo decides si un patrón vale la pena?**
Me hago tres preguntas: qué problema concreto resuelve aquí (no "algún día"), cuántas variantes existen hoy (con una o dos suele bastar un `if`; con la tercera, la regla de tres, abstraigo) y cuánto cuesta la indirección frente a lo que gana. Si no puedo escribir el dolor en una frase, no lo uso. Y si el lenguaje ya trae la solución (un generador, una función), uso eso.

**P3. Nombra tres antipatrones y su remedio.**
God Object: una clase con muchas responsabilidades; se separa por razón de cambio (SRP). Spaghetti code: `if` anidados por estado o tipo; se reemplazan con State o Strategy y funciones pequeñas. Singleton abuse: estado global escondido; se inyecta una única instancia desde el punto de arranque (DIP). Otros dos habituales son Golden Hammer y sobreingeniería, cuyo remedio es partir del problema, con KISS y YAGNI.

**P4. ¿Qué patrones usarías para un checkout y por qué?**
Una Facade como entrada única que coordina stock, precio, pago y estado, para que web, móvil y admin no repitan el protocolo. Decorator para el precio (cupón e IVA combinables), Strategy para el envío, Factory Method para elegir el notificador y State para el ciclo de vida del pedido. Observer (un bus de eventos) para avisar a inventario, correo y analítica sin acoplarlos. No usaría Singleton: la unicidad la da quien arma el programa.

**P5. ¿Qué patrones desaparecen en tu lenguaje favorito?**
En Python, Iterator es el `for` con generadores y Strategy suele ser pasar una función; Singleton casi es un módulo. En Go, Strategy es un tipo función, Builder es functional options, Factory Method es una función `NuevoX` y Iterator es `iter.Seq`. En TypeScript, Strategy, Command y Observer se resuelven bien con funciones y closures. No desaparece la idea, solo la jerarquía de clases que la implementaba.

**P6. Explica SOLID con un ejemplo en un minuto.**
Con la tienda: SRP, `Pedido` calcula su total y no envía correos; OCP, un envío nuevo es una clase nueva que implementa `EstrategiaEnvio`, sin editar el checkout. LSP, un `Combo` se usa donde se espera un producto sin sorpresas; ISP, quien solo notifica depende de `Notificador` y no de una interfaz gorda. DIP, el servicio depende de `MetodoPago` y no de `Webpay`.


## Preguntas transversales

**P1. ¿Qué patrón aplica OCP y cuáles te ayudan a evitar un `if` por tipo?**
Casi todos los patrones refuerzan [OCP](teoria/03-ocp.md) (abierto a extensión, cerrado a modificación), cada uno en un eje distinto. Para eliminar el `if` por tipo, Strategy ([módulo 16](teoria/16-strategy-state-template-method.md)) reemplaza el `if tipo_envio` por objetos intercambiables, State hace lo mismo con el `if estado`, y Factory Method ([módulo 08](teoria/08-factory-method.md)) concentra la decisión de qué clase crear. Decorator ([módulo 13](teoria/13-decorator-proxy.md)) agrega comportamiento apilando capas, y Visitor ([módulo 19](teoria/19-visitor-interpreter.md)) agrega operaciones nuevas sin tocar las clases, aunque ahí el trade-off es que un tipo de elemento nuevo obliga a editar todos los visitantes.

**P2. ¿Qué patrones se apoyan en la composición sobre la herencia, y cuáles en la herencia?**
Se apoyan en composición Strategy, State, Decorator, Proxy, Bridge, Adapter de objetos y Composite: un objeto guarda a otro y le delega, y esa referencia se puede cambiar sin tocar jerarquías. Los que usan herencia de forma central son Template Method (la clase base fija el esqueleto y las subclases rellenan pasos) y el Factory Method clásico (cada subclase del creador decide qué producto crea). Por eso Template Method está en tensión con "composición sobre herencia" ([módulo 16](teoria/16-strategy-state-template-method.md)), y en Go, que no tiene herencia, ambos se reescriben con funciones o interfaces ([módulo 08](teoria/08-factory-method.md)).

**P3. Adapter, Decorator, Proxy y Facade: ¿cómo los distingues en 30 segundos?**
Los cuatro envuelven a otros objetos y se separan por la interfaz y la intención. Adapter **cambia** la interfaz para que algo existente (un SDK) encaje en la que tu código espera. Decorator y Proxy **conservan** la misma interfaz: Decorator agrega comportamiento y se apila (`ConIVA(ConCupon(...))`), mientras que Proxy controla el acceso (caché, permisos, carga diferida). Facade define una interfaz **nueva y más pequeña** sobre varios objetos de un subsistema ([módulo 12](teoria/12-adapter-facade.md) y [módulo 13](teoria/13-decorator-proxy.md)).

**P4. ¿Qué patrones facilitan las pruebas unitarias y por qué?**
Todos los que dependen de una interfaz en lugar de una clase concreta, porque en la prueba se inyecta un doble (un repositorio en memoria, un notificador falso). La base es DIP con inyección por constructor ([módulo 06](teoria/06-dip.md)); Strategy permite probar cada algoritmo por separado, y Adapter y Proxy mantienen la interfaz del dominio, así que se pueden reemplazar por un `PagoFalso` o un catálogo falso. Observer permite probar al publicador con un suscriptor falso, sin conocer a los reales. En cambio Singleton las dificulta, porque es estado global que no se puede reemplazar y que persiste entre pruebas ([módulo 07](teoria/07-singleton.md)).

**P5. ¿Qué patrones casi desaparecen en Go o Python y por qué?**
Desaparecen los que existían para compensar carencias del lenguaje. Iterator se vuelve un `for`, un generador o `iter.Seq` (Go 1.23); Strategy y Command se reducen a una función, porque las funciones son valores; Factory Method se reduce a una función `NuevoX` que devuelve una interfaz; Builder se reemplaza por argumentos con nombre o *functional options*; y Singleton por un módulo de Python, que se evalúa una sola vez ([módulo 20](teoria/20-antipatrones-y-cierre.md)). En Go además Template Method no funciona con embedding, y Visitor suele sustituirse por un type switch ([módulo 16](teoria/16-strategy-state-template-method.md) y [módulo 19](teoria/19-visitor-interpreter.md)).

**P6. ¿Qué patrón elegirías para: añadir pagos nuevos, deshacer acciones, notificar a varios, crear objetos complejos, traducir un SDK?**
Pagos nuevos: Strategy, o Factory Method si además hay que elegir cuál crear, porque cada medio de pago es una clase nueva que cumple `MetodoPago` sin editar lo existente. Deshacer acciones: Command, que guarda cada acción como objeto con `ejecutar` y `deshacer` ([módulo 18](teoria/18-command-memento-iterator.md)); Memento si es más simple restaurar un estado guardado. Notificar a varios: Observer, porque el publicador no conoce a los suscriptores ([módulo 17](teoria/17-observer-mediator-chain.md)). Crear objetos complejos: Builder ([módulo 10](teoria/10-builder.md)), que valida antes de entregar el objeto. Traducir un SDK: Adapter, que convierte su interfaz (por ejemplo centavos) a `MetodoPago` ([módulo 12](teoria/12-adapter-facade.md)).

**P7. ¿Qué patrones conviven en un checkout real y cómo se combinan?**
En el caso de cierre del [módulo 20](teoria/20-antipatrones-y-cierre.md), `CheckoutFacade` es la puerta única y coordina el orden de los pasos. Dentro, un `CalculadorPrecio` decorado (`ConIVA(ConCupon(PrecioBase()))`) calcula el precio, una `EstrategiaEnvio` decide el envío, una fábrica entrega el `Notificador`, un `EstadoPedido` lleva el pedido de `Pendiente` a `Pagado`, y un `BusEventos` (Observer) avisa a otros sin que la fachada los conozca. Se combinan porque cada uno depende de una interfaz y la fachada los recibe por constructor, como en [DIP](teoria/06-dip.md).

**P8. Explica SOLID con un solo ejemplo de la tienda online.**
Tomemos el cobro de un pedido. SRP: el servicio de pedidos solo orquesta, y el envío de correos o el guardado viven en otras clases ([módulo 02](teoria/02-srp.md)). OCP: un medio de pago nuevo es una clase nueva que cumple `MetodoPago`, sin editar el servicio ([módulo 03](teoria/03-ocp.md)). LSP: cualquier `MetodoPago` debe poder usarse donde se espera uno sin sorpresas ([módulo 04](teoria/04-lsp.md)). ISP: el servicio depende de interfaces pequeñas, no de un `Notificador` que obligue a implementar métodos que no usa ([módulo 05](teoria/05-isp.md)). DIP: el servicio recibe esas interfaces por constructor y el composition root arma las clases concretas ([módulo 06](teoria/06-dip.md)).
