# Estructuras datos lineales

## Estructuras propias de python

Son estructuras propias de python: Listas, Tuplas, Conjuntos(Sets), Diccionarios. 

Estos tiene operaciones esenciales: 
- declararlas
- agregar elementos
- eliminar elementos
- ordenar los elementos
- insertar elementos en una posición determinada
- elimnar elementos en una posición determinada


## Tipos de colecciones

Para finales del curso cuando hablemos de colecciones también agregaremos a las estructuras de datos. 

¿Que es una colección? Grupo de cero o más elementos que pueden tratarse como una unidad conceptual. 

¿Por que cero o más? Recordemos que cero es un valor numérico, pero que Null o None es igual a nada. Además existen otros tipos de datos que son undefined (esto sucede en JavaScript cuando no esta definido que tipo de datos es)  

Las colecciones pueden ser: **dinamicas** (pueden aumentar o disminuir su tamano) o **inmutables** (no cambian su tamano)

De forma general podemos encontrar estructuras:
- ***lineales***: Ordenadas por posición o indice, solo el primer elemento no tiene predecesor. Ejemplos: fila en el supermercado, pila de platos, checklist.
- ***jerárquicas***: Ordenadas como un árbol invertido, solo el primer elemento no tiene predecesor, existen padres e hijos. Ejemplos: se puede imaginar como las carpetas de la pc, que tenemos más por dentro.
- ***grafos***: Cada grafo puede tener varios predecesores o sucesores, a los cuales se le llaman 'vecinos'. Ejemplos: rutas de vuelos áereos. 
- ***elementos ordenadas***: Pueden estar basadas en cualquiera de los tipos de colecciones anteriores, y generalmente tienen una regla de orden. Ejemplo: sería un catalogo de pinturas con un código, y el código tiene un orden definido. Otro ejemplo son las guías telefónicas donde se ordena de forma alfabética. 
- ***elementos desordenado***: No tiene un orden, no existen elementos sucesores o predecesores. Ejemplo sería una bolsa de bolitas, no sabemos cual nos va a tocar, ni el orden. 

Taxonomía de las colecciones de datos:
Colección:
        - Lineales:
            - Lista
                -Lista ordenada
            - Cola
                - Cola de prioridad
            - Pila
            - String
        - Jerárquica:
            - Árbol binario
            - Monticulo
        - Grafos
        - Desordenadas:
            - Bolsa
            - Diccionario
            - Conjunto

Vamos a centrarnos en las ***lineales***. Las estructuras de datos son herramientas y según el caso del software que vamos a desarrollar son las estructuras que vamos a implementar. 


## Operaciones esenciales en colecciones

Algunas de las operaciones son para conocer su tamaño, para saber si se encuentra dentro de una colección, recorrer dicha colección, convertirlo o representar en string, y saber si esa colección es igual a otra colección.  

Operaciones:
    - Tamano         - Concatenación
    - Pertenencia    - Conversión de tipo
    - Recorrido      - Insertar
    - String         - Remover
    - Iguladad       - Reemplazar
                     - Acceder 


## Colecciones incorporadas en Python

**LISTAS**: - Próposito general
            - Esctructura más utilizada
            - Tamano dinámico
            - De tipo secuencial
            - Ordenable

Es secuencial por que los elementos están definidos por un indice que comienza en cero y va aumentando de 1 en 1. 

**TUPLAS**: - Inmutable (no se puede anadir ni cambiar)
            - Útiles para datos constantes
            - Más rápidas que las listas
            - Tipo secuencial

Pueden servir para coordenadas de lugares, que sabemos que no van a cambiar.

**SETS**:   - Almacenan objetos no-duplicados 
            - De acceso rápido
            - Aceptan operaciones lógicas
            - Son desordenados

Operaciones lógicas: conjunción, disyunción. Un ejemplo es una receta de cocina. 

**DICCIONARIOS**:   - Pares de llave/valor 
                    - Arrays asociativos (hash maps)
                    - Son desordenados

Arrays asociativos, porque son arreglos asociados a un valor. Son bastante rápidos para realizar consultas. 


## Arrays

La primera estructura de datos que conoceremos serán los arrays. Una estructura de datos es la representación interna de una colección de información. Entonces un array tendrá información y va ser representado de una forma particular. 

Conceptos claves: * **elemento**: valor almacenado en las posiciones del array
                  * **índice**: referencia a la posición del elemento

Para entender mejor porque es conveniente utilizar arrays, hay que entender como funciona la memoria en la computadora: Podemos imaginarlo como una rejilla donde vamos a estar colocando datos. Podemos ocupar una o muchas casillas para almacenar información. 
Luego si borramos información se genera un espacio. Si queremos guardar nueva información esta se guardara en un lugar donde quepa. La importancia de los array es que guardan información de manera consecutiva y tiene ciertas restricciones. Entonces, al momento de guardar esa información no podremos guardar mas de lo que permite el array. En cambio una lista puede crecer de forma dinámica, y la información en este caso no será consecutiva, sino que va estar dispersa en la memoria. 

El array tiene una capacidad, y es el número de elementos que puede almacenar. Como ejemplo un array con una capacidad de 5 elementos, y sus indices que van del 0 al 4.  
Hay arrays de distinta dimensión. En python se recomienda que no trabajemos con estructuras de mas de dos dimensiones. Porque aumenta la complejidad de computo para acceder a los datos, y también el código se vuelve mas difícil de leer.

Acá surge una duda, ¿son los Array un tipo de listas? Si, pero las listas no son array. Los array son restrictivos: no pueden agregar posiciones, quitar posiciones, modificar su tamano, su capacidad se define al crearse. 

Un caso de uso pueden ser los videojuegos. En el caso de los gráficos de los videojuegos puede ser un mapa de bits, un array de dos dimensiones que tiene un largo y un alto. 
Las opciones del menú, puede ser otro ejemplo, ya que tenemos definido la cantidad de opciones de ante mano. 

Python cuenta con un modulo de Array pero no es tan versátil como queremos, ya que solo almacena números y caracteres y ademas esta basado en listas. 


## Creando un Array

Los array pueden tener los siguientes métodos: * Crearse
                                               * Longitud o tamano
                                               * Representación en string
                                               * Pertenencia, si está presente el elemento
                                               * Índice
                                               * Reemplazo

Creamos el ***archivo class_1.py***
Cree también el archivo ***reto_clase_7.py***, se pedía agregar un método para poblar sus slots con números aleatorios, y también un método que sume todos los valores del array. 


## Arrays de dos dimensiones

Los array de dos dimensiones se nombran de varias formas: Bi-demensional array, Two-dimensional array, Grid, Rejilla, Malla, Tabla. 

Creamos el archivo class_2.py. 

No es conveniente realizar un array de 3 dimensiones, pero igualmente vamos hacerlo para el reto. Ver archivos reto_clase_8.1.py y reto_clase_8.12.py


## Nodos y singly linked list

Linked structures: - Consiste de nodos conectados a otros nodos
                   - Los más comunes son sencillos o dobles
                   - No se accede por índice, sino por recorrido

Conceptos claves: * Data: valor almacenado en los nodos
                  * Next: referencia al proximo valor
                  * Previous: referencia al nodo anterior
                  * Head: referencia al primer nodo
                  * Tail: referencia al último nodo

Los datos de los nodos están repartidos en la memoria. Esto nos da la ventaja de que podemos acceder a los datos saltando en los espacios de memoria de una forma ágil. Los podemos usar para implementar otras estructuras, optimización.
Ejemplos de uso: hacer/rehacer operaciones en un editor de texto, historial de un navegador. 


## Crear nodos

Ver archivo ***class_3.py***

Hay que tener en cuenta que las conexiones o referencias entre nodos pueden llegar a ser complejas, si llegamos a tener mucha información. Por lo tanto es conveniente hacerlo ordenado. 

Con un ciclo while creamos una serie de nodos, donde cada uno tenía un valor correlativo, y además se conectaban con el siguiente nodo. 
Con los ciclos (while and for) podemos traer información que esta en un archivo o una lista, de manera desordenada, las acomodamos a nodos y por lo tanto sus referencias serán más claras, y mas ágiles al momento de consultarlas. 

Bonus: 
Crear singly linked list: ver archivo ***singly_linked_list.py***


## Operaciones con single linked structures

Hay un problema con estas single linked list, y es que no tienen un indice. No hay algo que nos diga este es el nodo 1, este es el nodo 3 , etc. Por lo tanto debemos de emular ese indice. 

Una de las operaciones más comunes es el de recorrido, que es donde usamos el índice. Utilizaremos una variable llamada **probe**, como sonda en español. 

Haremos de ejemplo que los nodos, son como planetas, donde en cada uno de ellos hay información. Y en vez de tener que consultar cada uno, podemos utilizar esta variable para que los recorra consulte los datos, y así podemos hacer más cosas. 

ver archivo ***singly_linked_list_2.py***


## Doble linked list

Las listas dobles se llaman así porque el sentido en el que funcionan los punteros no es en una sola vía. Un puntero hace referencia al siguiente nodo y al anterior. 

En el caso del primer nodo solo hará referencia al primero. También se puede hacer que haga referencia al primero, y de esta forma será una circular double linked list. 

Haremos un archivo llamado double_linked_list.py. Tendremos dos tipos de nodos, el que ya utilizamos y otro TwoWayNode() 


## Stacks

Principio LIFO = Last in, first out

Cuando realizamos control + z en word esa información seguro esta en una pila, por lo que vamos sacando los elementos que colocamos, hasta volver a la situación que deseamos. Reaalizamos pop() en este caso.

Para crear un stack lo podemos hacer con nodos o con arrays. Lo vamos hacer con nodos. La diferencia es que al igual que en las linked list, cuando agregamos muchos nodos, se empieza hacer más complejo nuestro código. Si sabemos cuantos elementos van haber en el stack o hay un limite máximo, lo mejor es utilizar arrays. En el caso de ser pocos elementos podemos utilizar nodos. 


## Queue

Principio FIFO = first in, first out

Funciona igual que el anterior, pero sus elementos  pueden tener una prioridad distinta a ser atendida. Esto puede suceder en un aeropuerto, con el abordaje de los aviones.