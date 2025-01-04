# Little Sister's Essay

Bienvenido al ensayo de Little Sister sobre el curso de Python en Exercism.  
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, revisa el archivo `HELP.md`.  
Si te quedas atascado en el ejercicio, consulta `HINTS.md`, pero intenta resolverlo por tu cuenta primero. :)

## Introducción

La clase `str` ofrece [muchos métodos útiles][str methods] para trabajar y manipular cadenas de texto.  
Entre ellos se incluyen búsqueda, limpieza, división, transformación, traducción y otras técnicas.  

Las cadenas son [secuencias inmutables][text sequence] de [puntos de código Unicode][unicode code points], donde cada "carácter" o punto de código (_cadenas de longitud 1_) puede ser referenciado por su índice basado en 0 desde la izquierda o índice basado en -1 desde la derecha.

Puedes iterar sobre una cadena usando la sintaxis `for item in <str>` o `for index, item in enumerate(<str>)`.  
Se pueden concatenar cadenas con el operador `+` o mediante `<string>.join(<iterable>)`, además de implementar todas las [operaciones comunes de secuencias][common sequence operations].  

Las cadenas son _inmutables_, lo que significa que el valor de un objeto `str` en memoria no puede cambiar.  
Las funciones o métodos que operan sobre una cadena (_como los que veremos aquí_) devolverán una nueva instancia de ese objeto `str`, en lugar de modificar el original.

A continuación, se muestra una pequeña selección de métodos de cadenas en Python.  
Para una lista completa, consulta la [clase `str`][str methods] en la documentación de Python.

### Ejemplo: Métodos de cadenas

[`<str>.title()`][str-title] analiza una cadena y capitaliza el primer "carácter" de cada "palabra" encontrada.  
En Python, esto depende mucho del [códec de idioma][codecs] usado y de cómo ese idioma representa palabras y caracteres. También pueden influir las reglas de [localización][locale] específicas para un idioma o conjunto de caracteres.

```python
man_in_hat_th = 'ผู้ชายใส่หมวก'
man_in_hat_ru = 'мужчина в шляпе'
man_in_hat_ko = '모자를 쓴 남자'
man_in_hat_en = 'the man in the hat.'

>>> man_in_hat_th.title()
'ผู้ชายใส่หมวก'

>>> man_in_hat_ru.title()
'Мужчина В Шляпе'

>>> man_in_hat_ko.title()
'모자를 쓴 남자'

>>> man_in_hat_en.title()
'The Man In The Hat.'
```

[`<str>.endswith(<suffix>)`][str-endswith] devuelve `True` si la cadena termina con `<suffix>` y `False` en caso contrario.

```python
>>> 'My heart breaks. 💔'.endswith('💔')
True

>>> 'cheerfulness'.endswith('ness')
True

# La puntuación es parte de la cadena, por lo que debe incluirse en cualquier comparación.
>>> 'Do you want to 💃?'.endswith('💃')
False

>>> 'The quick brown fox jumped over the lazy dog.'.endswith('dog')
False
```

[`<str>.strip(<chars>)`][str-strip] devuelve una copia de la cadena con los caracteres iniciales y finales `<chars>` eliminados.  
Los puntos de código especificados en `<chars>` no son un prefijo ni un sufijo; **todas las combinaciones** de estos puntos de código se eliminan comenzando por **ambos extremos** de la cadena.  
Si no se especifica nada en `<chars>`, se eliminarán todas las combinaciones de espacios en blanco.

```python
# Esto elimina "https://", porque puede formarse a partir de "/stph:".
>>> 'https://unicode.org/emoji/'.strip('/stph:')
'unicode.org/emoji'

# Eliminación de todos los espacios en blanco de ambos extremos de la cadena.
>>> '   🐪🐪🐪🌟🐪🐪🐪   '.strip()
'🐪🐪🐪🌟🐪🐪🐪'

>>> justification = 'оправдание'
>>> justification.strip('еина')
'оправд'

# Eliminación de prefijo y sufijo en un solo paso.
>>> 'unaddressed'.strip('dnue')
'address'

>>> '  unaddressed  '.strip('dnue ')
'address'
```

[`<str>.replace(<substring>, <replacement substring>)`][str-replace] devuelve una copia de la cadena con todas las ocurrencias de `<substring>` reemplazadas por `<replacement substring>`.

El ejemplo a continuación utiliza una cita de [The Hunting of the Snark][The Hunting of the Snark] de [Lewis Carroll][Lewis Carroll].

```python
# The Hunting of the Snark, por Lewis Carroll
>>> quote = '''
"Just the place for a Snark!" the Bellman cried,
   As he landed his crew with care;
Supporting each man on the top of the tide
   By a finger entwined in his hair.

"Just the place for a Snark! I have said it twice:
   That alone should encourage the crew.
Just the place for a Snark! I have said it thrice:
   What I tell you three times is true."
'''

>>> quote.replace('Snark', '🐲')
...
'\n"Just the place for a 🐲!" the Bellman cried,\n   As he landed his crew with care;\nSupporting each man on the top of the tide\n   By a finger entwined in his hair.\n\n"Just the place for a 🐲! I have said it twice:\n   That alone should encourage the crew.\nJust the place for a 🐲! I have said it thrice:\n   What I tell you three times is true."\n'

>>> 'bookkeeper'.replace('kk', 'k k')
'book keeper'
```


## Instrucciones

En este ejercicio, estás ayudando a tu hermana menor a editar su ensayo para la escuela.  
La profesora está buscando puntuación correcta, gramática adecuada y un excelente uso del lenguaje.  

Tendrás cuatro tareas para limpiar y modificar cadenas de texto.

---

### 1. Capitalizar el título del ensayo

Todo buen ensayo necesita un título correctamente formateado.  
Implementa la función `capitalize_title(<title>)`, que toma como parámetro un título de tipo `str` y capitaliza la primera letra de cada palabra.  
Esta función debe devolver una cadena en formato de título.

```python
>>> capitalize_title("my hobbies")
"My Hobbies"
```

---

### 2. Verificar si cada oración termina con un punto

Es importante asegurarte de que la puntuación del ensayo sea perfecta.  
Implementa la función `check_sentence_ending()` que toma como parámetro `sentence`. Esta función debe devolver un valor booleano (`bool`).

```python
>>> check_sentence_ending("I like to hike, bake, and read.")
True
```

---

### 3. Limpiar los espacios en blanco

Para que el ensayo se vea profesional, es necesario eliminar los espacios innecesarios.  
Implementa la función `clean_up_spacing()` que toma como parámetro `sentence`.  
La función debe eliminar el espacio extra al principio y al final de la oración, devolviendo una nueva cadena (`str`) actualizada.

```python
>>> clean_up_spacing(" I like to go on hikes with my dog.  ")
"I like to go on hikes with my dog."
```

---

### 4. Reemplazar palabras con un sinónimo

Para hacer el ensayo _aún mejor_, puedes reemplazar algunos adjetivos con sus sinónimos.  
Escribe la función `replace_word_choice()` que toma como parámetros `sentence`, `old_word` y `new_word`.  
Esta función debe reemplazar todas las ocurrencias de `old_word` con `new_word`, devolviendo una nueva cadena (`str`) con la oración actualizada.

```python
>>> replace_word_choice("I bake good cakes.", "good", "amazing")
"I bake amazing cakes."
```

## Source

### Created by

- @kimolivia

### Contributed to by

- @valentin-p
- @BethanyG