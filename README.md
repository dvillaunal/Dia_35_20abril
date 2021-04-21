# Python Collections Module:
* Link de referencia:
  [libreria Collections](https://rico-schmidt.name/pymotw-3/collections/)

El módulo de colección en Python proporciona diferentes tipos de contenedores. Un contenedor es un objeto que se utiliza para almacenar diferentes objetos y proporcionar una forma de acceder a los objetos contenidos e iterar sobre ellos. Algunos de los contenedores integrados son Tuple , List , Dictionary , etc.

#### Nota:
Para obtener más información, consulte [Contadores en Python.](https://stackabuse.com/introduction-to-pythons-collections-module/)

## ``Counter()``:

Un contador es una subclase del diccionario. __Se utiliza para mantener el recuento de los elementos en un iterable en forma de diccionario desordenado__ donde la clave representa el elemento en el iterable y el valor representa el recuento de ese elemento en el iterable.


### Sintaxis:

~~~
class collections.Counter([iterable-or-(mapeo or mapping)])
~~~

### Inicializar objetos de contador:
 
 El objeto contador se puede inicializar utilizando la función ``Counter()`` y esta función se puede llamar de una de las siguientes formas:
   - Con una secuencia de elementos.

   - Con un diccionario que contiene claves y recuentos.

   - Con argumentos de palabras clave que mapean nombres de   cadenas a recuentos.
  



## ``OrderedDict()``:

Un OrderedDict también es una subclase de diccionario pero, a diferencia de un diccionario, recuerda el orden en el que se insertaron las claves. 

### Sintaxis:

~~~
class collections.OrderDict()
~~~

## ``DefaultDict``:

Un DefaultDict también es una subclase del diccionario. Se utiliza para proporcionar algunos valores predeterminados para la clave que no existe y nunca genera un ``KeyError``.

### Sintaxis:

~~~
class collections.defaultdict(default_factory)
~~~

 * ``default_factory`` _es una función que proporciona el     valor predeterminado para el diccionario creado. Si este   parámetro está ausente, se genera KeyError._


### Inicialización de objetos DefaultDict():

Los objetos DefaultDict se pueden inicializar usando el método ``DefaultDict()`` pasando el tipo de datos como un argumento.

## ``ChainMap``:

Un ``ChainMap()`` encapsula muchos diccionarios en una sola unidad y devuelve una lista de diccionarios.


### Acceder a claves y valores desde ``ChainMap()``:

Se puede acceder a los valores de ``ChainMap`` utilizando el nombre de la clave. También se puede acceder a ellos mediante el método de ``keys()`` y ``values()``.


## _Comentario_: 
_Creo que [Replit](https://replit.com/) tiene nativo la libreria ``Collections`` ya que no tuve que cargar ningua archivo donde guarde la información que descarga de otros servidores._

 >___ejemplo:___
  
  > _para utilizar pandas descargaba en el repositorio unos   archivos donde contenia la libreria pd, ahora con         ``collections`` no lo hizo eso me hace suponer que sus    servidores las tienen precargadas._



