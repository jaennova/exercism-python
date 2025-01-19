# Little Sister's Vocabulary

Bienvenido a **Little Sister's Vocabulary** en la sección de Python de Exercism.  
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, revisa el archivo `HELP.md`.  
Si te atascas con el ejercicio, consulta el archivo `HINTS.md`, pero intenta resolverlo sin usarlo primero. 😊

---

## Introducción

Un `str` en Python es una [secuencia inmutable][text sequence] de [puntos de código Unicode][unicode code points].  
Esto incluye letras, marcas diacríticas, caracteres de posicionamiento, números, símbolos de moneda, emojis, signos de puntuación, espacios, saltos de línea, entre otros.  
Dado que es inmutable, el valor de un objeto `str` en memoria no cambia. Los métodos que parecen modificar una cadena devuelven una nueva copia o instancia del objeto `str`.

Una literal `str` se puede declarar usando comillas simples `'` o dobles `"`. El carácter de escape `\` está disponible cuando sea necesario.

```python
>>> single_quoted = 'Estas permiten usar "comillas dobles" sin necesidad de caracteres de escape.'

>>> double_quoted = "Estas permiten incluir 'comillas simples', así que no necesitas usar un carácter de escape."

>>> escapes = 'Si es necesario, una barra invertida \\ puede usarse como carácter de escape dentro de una cadena, cuando cambiar el estilo de comillas no sea suficiente.'
```

Las cadenas de varias líneas se declaran con `'''` o `"""`.

```python
>>> triple_quoted = '''Tres comillas simples o dobles seguidas permiten literales de varias líneas.
  Los saltos de línea, tabulaciones y otros espacios en blanco son totalmente compatibles.

  A menudo las encontrarás como "doc strings" o "doc tests", escritas justo debajo de la definición de una función o clase.
  Suelen usarse con herramientas de documentación automática ✍.'''
```

Las cadenas pueden concatenarse utilizando el operador `+`.  
Este método debe usarse con moderación, ya que no es muy eficiente ni fácil de mantener.

```python
language = "Ucraniano"
number = "nueve"
word = "дев'ять"

sentence = word + " " + "significa" + " " + number + " en " + language + "."

>>> print(sentence)
...
"дев'ять significa nueve en Ucraniano."
```

Si necesitas combinar elementos individuales de una `list`, `tuple`, `set` u otra colección de cadenas en un solo `str`, [`<str>.join(<iterable>)`][str-join] es una mejor opción:

```python
# str.join() crea una nueva cadena a partir de los elementos de un iterable.
>>> chickens = ["hen", "egg", "rooster"]
>>> ' '.join(chickens)
'hen egg rooster'

# Cualquier cadena puede usarse como elemento de unión.
>>> ' :: '.join(chickens)
'hen :: egg :: rooster'

>>> ' 🌿 '.join(chickens)
'hen 🌿 egg 🌿 rooster'
```

Los puntos de código dentro de un `str` pueden referenciarse mediante índices basados en 0 desde la izquierda:

```python
creative = '창의적인'

>>> creative[0]
'창'

>>> creative[2]
'적'

>>> creative[3]
'인'
```

El índice también funciona desde la derecha, comenzando con un índice basado en -1:

```python
creative = '창의적인'

>>> creative[-4]
'창'

>>> creative[-2]
'적'

>>> creative[-1]
'인'
```

No existe un tipo separado para “caracteres” o "runes" en Python, por lo que indexar una cadena produce un nuevo `str` de longitud 1:

```python
>>> website = "exercism"
>>> type(website[0])
<class 'str'>

>>> len(website[0])
1

>>> website[0] == website[0:1] == 'e'
True
```

Puedes seleccionar subcadenas utilizando _slice notation_ (`<str>[<start>:<stop>:<step>]`), lo que genera una nueva cadena.  
El resultado excluye el índice `stop`. Si no se proporciona un `start`, el índice inicial será 0. Si no se proporciona un `stop`, el índice final será el final de la cadena.

```python
moon_and_stars = '🌟🌟🌙🌟🌟⭐'
sun_and_moon = '🌞🌙🌞🌙🌞🌙🌞🌙🌞'

>>> moon_and_stars[1:4]
'🌟🌙🌟'

>>> moon_and_stars[:3]
'🌟🌟🌙'

>>> moon_and_stars[3:]
'🌟🌟⭐'

>>> moon_and_stars[:-1]
'🌟🌟🌙🌟🌟'

>>> moon_and_stars[:-3]
'🌟🌟🌙'

>>> sun_and_moon[::2]
'🌞🌞🌞🌞🌞'

>>> sun_and_moon[:-2:2]
'🌞🌞🌞🌞'

>>> sun_and_moon[1:-1:2]
'🌙🌙🌙🌙'
```

Las cadenas también pueden dividirse en subcadenas utilizando [`<str>.split(<separator>)`][str-split], lo que devuelve una `list` de subcadenas.  
La lista resultante puede indexarse o dividirse aún más si es necesario. Si usas `<str>.split()` sin argumentos, la cadena se dividirá por espacios en blanco.

```python
>>> cat_ipsum = "Destruye la casa en 5 segundos, burla al humano."
>>> cat_ipsum.split()
...
['Destruye', 'la', 'casa', 'en', '5', 'segundos,', 'burla', 'al', 'humano.']

>>> cat_ipsum.split()[-1]
'humano.'

>>> cat_words = "felino, cuadrúpedo, feroz, peludo"
>>> cat_words.split(', ')
...
['felino', 'cuadrúpedo', 'feroz', 'peludo']
```

Los separadores para `<str>.split()` pueden contener más de un carácter.  
Toda la cadena proporcionada como separador se utiliza para realizar la división.

```python
>>> colors = """rojo,
naranja,
verde,
morado,
amarillo"""

>>> colors.split(',\n')
['rojo', 'naranja', 'verde', 'morado', 'amarillo']
```

---

Las cadenas soportan todas las [operaciones comunes de secuencia][common sequence operations].  
Puedes iterar sobre cada punto de código en una cadena utilizando un bucle `for item in <str>`.  
Si necesitas tanto los índices como los elementos, usa `for index, item in enumerate(<str>)`.

```python
>>> exercise = 'လေ့ကျင့်'

# Nota: Hay más puntos de código que glifos o caracteres percibidos.
>>> for code_point in exercise:
...    print(code_point)
...
လ
ေ
့
က
ျ
င
်
့

# Usar enumerate proporciona tanto el índice como el valor de cada elemento.
>>> for index, code_point in enumerate(exercise):
...    print(index, ": ", code_point)
...
0 :  လ
1 :  ေ
2 :  ့
3 :  က
4 :  ျ
5 :  င
6 :  ်
7 :  ့
```

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations  
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join  
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split  
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str  
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme  


## Instrucciones

Estás ayudando a tu hermana menor con su tarea de vocabulario en inglés, la cual encuentra bastante tediosa.  
Su clase está aprendiendo a crear nuevas palabras añadiendo _prefijos_ y _sufijos_.  
Dado un conjunto de palabras, la maestra busca transformaciones correctas con la ortografía adecuada al añadir el prefijo al inicio o el sufijo al final.

La tarea tiene cuatro actividades, cada una con un conjunto de textos o palabras para trabajar.

---

### 1. Añadir un prefijo a una palabra

Uno de los prefijos más comunes en inglés es `un`, que significa "no".  
En esta actividad, tu hermana necesita crear palabras negativas, o que signifiquen "no", añadiendo `un` al inicio.

Implementa la función `add_prefix_un(<word>)`, que toma `word` como parámetro y devuelve una nueva palabra con el prefijo `un` añadido:

```python
>>> add_prefix_un("happy")
'unhappy'

>>> add_prefix_un("manageable")
'unmanageable'
```

---

### 2. Añadir prefijos a grupos de palabras

Existen otros cuatro prefijos comunes que la clase de tu hermana está estudiando:  
- `en` (_que significa 'poner en' o 'cubrir con'_),  
- `pre` (_que significa 'antes' o 'hacia adelante'_),  
- `auto` (_que significa 'auto' o 'igual'_),  
- y `inter` (_que significa 'entre' o 'entre varios'_).  

En este ejercicio, la clase está creando grupos de palabras con estos prefijos para estudiarlos juntos.  
Cada prefijo viene acompañado de una lista de palabras comunes con las que se utiliza.  
Los estudiantes deben aplicar el prefijo y producir una cadena que muestre el prefijo aplicado a todas las palabras.

Implementa la función `make_word_groups(<vocab_words>)`, que toma `vocab_words` como parámetro en el siguiente formato:  
`[<prefix>, <word_1>, <word_2>, ..., <word_n>]`  
y devuelve una cadena con el prefijo aplicado a cada palabra, de la forma:  
`'<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'`.

```python
>>> make_word_groups(['en', 'close', 'joy', 'lighten'])
'en :: enclose :: enjoy :: enlighten'

>>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
'pre :: preserve :: predispose :: preposition'

>>> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
'auto :: autodidactic :: autograph :: automate'

>>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
'inter :: intertwine :: interconnected :: interdependent'
```

---

### 3. Eliminar un sufijo de una palabra

El sufijo `ness` es común y significa _'estado de ser'_.  
En esta actividad, tu hermana necesita encontrar la raíz original de la palabra eliminando el sufijo `ness`.  
Pero hay reglas de ortografía: Si la raíz terminaba originalmente en una consonante seguida de una 'y', entonces la 'y' se cambió a 'i'.  
Eliminar `ness` debe restaurar la 'y' en esas palabras raíz. Por ejemplo:  
`happiness` → `happi` → `happy`.

Implementa la función `remove_suffix_ness(<word>)`, que toma un `word` como entrada y devuelve la palabra raíz sin el sufijo `ness`.

```python
>>> remove_suffix_ness("heaviness")
'heavy'

>>> remove_suffix_ness("sadness")
'sad'
```

---

### 4. Extraer y transformar una palabra

Los sufijos a menudo se usan para cambiar la categoría gramatical de una palabra.  
Una práctica común en inglés es "verbing" o "verbificar", donde un adjetivo se convierte en verbo al añadir el sufijo `en`.

En esta tarea, tu hermana va a practicar "verbificar" palabras extrayendo un adjetivo de una oración y transformándolo en un verbo.  
Afortunadamente, todas las palabras que necesitan transformarse aquí son "regulares", es decir, no requieren cambios ortográficos para añadir el sufijo.

Implementa la función `adjective_to_verb(<sentence>, <index>)`, que toma dos parámetros:  
Una oración (`sentence`) que contiene la palabra a transformar y el índice (`index`) de esa palabra una vez que la oración se divide en palabras.  
La función debe devolver el adjetivo extraído como un verbo.

```python
>>> adjective_to_verb('I need to make that bright.', -1)
'brighten'

>>> adjective_to_verb('It got dark as the sun set.', 2)
'darken'
```


## Source

### Created by

- @aldraco
- @BethanyG