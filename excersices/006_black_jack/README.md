### Black Jack

Bienvenido al proyecto **Black Jack** en la sección de Python en **Exercism**.  
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, revisa el archivo `HELP.md`.  
Si te quedas atascado en el ejercicio, consulta `HINTS.md`, pero intenta resolverlo por tu cuenta primero. 😊

---

### Introducción

#### Comparaciones

Python admite los siguientes operadores básicos de comparación:

| Operador | Operación                  | Descripción                                                                 |
|----------|----------------------------|-----------------------------------------------------------------------------|
| `>`      | "mayor que"                | `a > b` es `True` si `a` es **estrictamente** mayor en valor que `b`.       |
| `<`      | "menor que"                | `a < b` es `True` si `a` es **estrictamente** menor en valor que `b`.       |
| `==`     | "igual a"                  | `a == b` es `True` si `a` es **exactamente igual** a `b` en valor.          |
| `>=`     | "mayor o igual que"        | `a >= b` es `True` si `a > b` **o** `a == b`.                               |
| `<=`     | "menor o igual que"        | `a <= b` es `True` si `a < b` **o** `a == b`.                               |
| `!=`     | "no igual a"               | `a != b` es `True` si `a == b` es `False`.                                  |
| `is`     | "identidad"                | `a is b` es `True` si **_y solo si_** `a` y `b` son el mismo _objeto_.      |
| `is not` | "identidad negada"         | `a is not b` es `True` si `a` y `b` **no** son el mismo _objeto_.           |
| `in`     | "prueba de pertenencia"    | `a in b` es `True` si `a` es miembro, subconjunto o elemento de `b`.        |
| `not in` | "prueba de no pertenencia" | `a not in b` es `True` si `a` no es miembro, subconjunto o elemento de `b`. |

Todos estos operadores tienen la misma prioridad (_que es más alta que las [operaciones booleanas][boolean operations],
pero más baja que las operaciones aritméticas o bit a bit_).

---

#### Comparación entre diferentes tipos de datos

Por defecto, los objetos de diferentes tipos (_excepto tipos numéricos_) nunca se consideran iguales.  
Las instancias no idénticas de una `class` tampoco serán iguales a menos que la clase implemente métodos
de [comparación avanzada][rich comparisons] que personalicen este comportamiento. Esto se verá en ejercicios
posteriores.  
Para más detalles, revisa la sección de [Comparaciones de valores][value comparisons] en la documentación de Python.

Los tipos numéricos son una excepción parcial a esta regla.  
Por ejemplo, un `integer` puede ser igual a un `float` (_o un [`octal`][octal] igual a un [`hexadecimal`][hex]_),
siempre que puedan convertirse implícitamente para realizar la comparación.

Para otros tipos numéricos de la biblioteca
estándar ([números complejos][complex numbers], [decimales][decimal numbers], [fracciones][rational numbers]), los
operadores de comparación funcionan donde tiene sentido (_donde la conversión implícita no altera el resultado_), pero
lanzan un `TypeError` si los objetos no pueden convertirse con precisión.  
Más información sobre las reglas de conversión en [conversiones aritméticas][arithmetic conversions] en la documentación
de Python.

```python
>> > import fractions

# Una cadena no puede convertirse a entero.
>> > 17 == '17'
False

# Un entero puede convertirse a flotante para comparar.
>> > 17 == 17.0
True

# La fracción 6/3 se convierte en el entero 2,
# y este puede representarse como 0b10 en binario.
>> > 6 / 3 == 0b10
True

# Un entero se convierte a número complejo con parte imaginaria 0.
>> > 17 == complex(17)
True

# La fracción 2/5 se convierte al flotante 0.4.
>> > 0.4 == 2 / 5
True

>> > complex(2 / 5, 1 / 2) == complex(0.4, 0.5)
True
```

Cualquier comparación ordenada de un número con un tipo `NaN` (_not a number_) siempre es `False`.  
Un efecto confuso del `NaN` en Python es que nunca se considera igual a sí mismo.

```python
>> > x = float('NaN')

>> > 3 < x
False

>> > x < 3
False

# NaN nunca es igual a NaN
>> > x == x
False
```

Claro, aquí tienes la continuación adaptada:

---

## Comparación de Cadenas

A diferencia de los números, las cadenas (`str`) se comparan de manera **lexicográfica**, utilizando sus puntos de
código Unicode individuales (el resultado de pasar cada punto de código de la cadena a la función incorporada `ord()`,
que devuelve un `int`).  
Si todos los puntos de código en ambas cadenas coinciden y están **en el mismo orden**, las dos cadenas se consideran
iguales.  
Esta comparación se realiza de manera "pareada": primero con el primer carácter, luego con el segundo, y así
sucesivamente.  
En Python 3.x, no se puede comparar directamente una cadena (`str`) con un objeto `bytes`.

```python
>> > 'Python' > 'Rust'
False

>> > 'Python' > 'JavaScript'
True

# Ejemplos con mandarín.
# hello < goodbye
>> > '你好' < '再见'
True

# ord() de los primeros caracteres
>> > ord('你'), ord('再')
(20320, 20877)

# ord() de los segundos caracteres
>> > ord('好'), ord('见')
(22909, 35265)

# Y con palabras en coreano.
# Pretty < beautiful.
>> > '예쁜' < '아름다운'
False

>> > ord('예'), ord('아')
(50696, 50500)
```

---

## Encadenamiento de Comparaciones

Los operadores de comparación pueden ser encadenados de manera **arbitraria**, lo que significa que se pueden usar en
cualquier combinación y longitud.  
Es importante tener en cuenta que la evaluación de una expresión se realiza de **izquierda a derecha**.

Por ejemplo, `x < y <= z` es equivalente a `x < y` **y** `y <= z`, excepto que `y` se evalúa **solo una vez**.  
En ambos casos, `z` no se evalúa **en absoluto** cuando se encuentra que `x < y` es `False`.  
Esto se llama **evaluación de cortocircuito**: la evaluación se detiene si el valor de verdad de la expresión ya ha sido
determinado.

El **cortocircuito** es soportado por varios operadores booleanos, funciones y también por el encadenamiento de
comparaciones en Python.  
A diferencia de muchos otros lenguajes de programación, incluyendo `C`, `C++`, `C#`, y `Java`, las expresiones
encadenadas como `a < b < c` en Python tienen una interpretación convencional **matemática** y una precedencia especial.

```python
>> > x = 2
>> > y = 5
>> > z = 10

>> > x < y < z
True

>> > x < y > z
False

>> > x > y < z
False
```

---

## Comparación de Identidad de Objetos

Los operadores `is` y `is not` prueban la **identidad** del objeto, a diferencia de la comparación de **valores**.  
La identidad de un objeto nunca cambia después de su creación y puede ser obtenida usando la función incorporada `id()`.

`<manzana> is <naranja>` devuelve `True` **solo si** `id(<manzana>)` == `id(<naranja>)`.  
`<manzana> is not <naranja>` devuelve el valor contrario.

Debido a su estatus de singleton, `None` y `NotImplemented` siempre deben compararse con otros objetos usando `is` y
`is not`.  
Consulta la documentación de Python
sobre [comparaciones de valor](https://docs.python.org/3/reference/expressions.html?highlight=none#value-comparisons)
y [PEP8](https://pep8.org/#programming-recommendations) para más detalles sobre esta convención.

```python
>> > mis_numeros_favoritos = [1, 2, 3]

>> > tus_numeros_favoritos = mis_numeros_favoritos

>> > mis_numeros_favoritos is tus_numeros_favoritos
True

# El id retornado variará dependiendo del sistema y la versión de Python.
>> > id(mis_numeros_favoritos)
4517478208

# tus_numeros_favoritos es solo un alias que apunta al objeto original mis_numeros_favoritos.
# Asignar un nuevo nombre no crea un nuevo objeto.
>> > id(tus_numeros_favoritos)
4517478208

>> > mis_numeros_favoritos is not tus_numeros_favoritos
False

>> > mis_numeros_favoritos is None
True

>> > mis_numeros_favoritos is NotImplemented
False
```

---

## Membership comparisons

Los operadores `in` y `not in` prueban la _pertenencia_.
`<fish> in <soup>` devuelve `True` si `<fish>` es un miembro de `<soup>` (_si `<fish>` es un subconjunto de o está
contenido dentro de `<soup>`_), y devuelve `False` en caso contrario.
`<fish> not in <soup>` devuelve la negación, o _opuesto de_ `<fish> in <soup>`.

Para los tipos de cadena y bytes, `<name> in <fullname>` es `True` _**si y solo si**_ `<name>` es un subcadena de
`<fullname>`.

```python
# Un conjunto de números de la suerte.
>> > lucky_numbers = {11, 22, 33}
>> > 22 in lucky_numbers
True

>> > 44 in lucky_numbers
False

# Un diccionario con información de empleados.
>> > employee = {'name': 'John Doe',
                 'id': 67826, 'age': 33,
                 'title': 'ceo'}

# Verificando la pertenencia de ciertas claves.
>> > 'age' in employee
True

>> > 33 in employee
False

>> > 'lastname' not in employee
True

# Verificando la pertenencia de subcadenas
>> > name = 'Super Batman'
>> > 'Bat' in name
True

>> > 'Batwoman' in name
False
```

## Instructions

En este ejercicio vas a implementar algunas reglas del [Blackjack][blackjack], como la forma en que se juega y se
puntúa.

**Nota**: En este ejercicio, _`A`_ significa as, _`J`_ significa jack, _`Q`_ significa reina, y _`K`_ significa rey. Los
comodines se descartan. Se asume que se usa una [baraja francesa estándar de 52 cartas][standard_deck], pero en muchas
versiones se barajan varias barajas juntas para jugar.

### 1. Calcular el valor de una carta

En Blackjack, es responsabilidad de cada jugador decidir si un as vale 1 o 11 puntos (_más sobre eso más adelante_).
Las cartas con figura (`J`, `Q`, `K`) valen 10 puntos, y cualquier otra carta vale su valor numérico.

Define la función `value_of_card(<card>)` con el parámetro `card`.
La función debe devolver el _valor numérico_ de la carta pasada como parámetro.
Dado que un as puede tener varios valores (1 **o** 11), por ahora fija el valor del as en 1.
Más adelante, implementarás una función para determinar el valor de un as, dada una mano existente.

```python
>> > value_of_card('K')
10

>> > value_of_card('4')
4

>> > value_of_card('A')
1
```

### 2. Determinar qué carta tiene un valor más alto

Define la función `higher_card(<card_one>, <card_two>)` con los parámetros `card_one` y `card_two`.
Para efectos de puntuación, las cartas `J`, `Q` o `K` valen 10.
La función debe devolver cuál de las dos cartas tiene el valor más alto para puntuar.
Si ambas cartas tienen el mismo valor, devuelve ambas.
Para devolver ambas cartas, puedes usar una coma en la declaración `return`:

```python
# Usar una coma en un return crea una tupla. Las tuplas se cubrirán en un ejercicio posterior.
>> >

def returning_two_values(value_one, value_two):
    return value_one, value_two

>> > returning_two_values('K', '3')
('K', '3')
```

Un as puede tener múltiples valores, así que para este ejercicio fija las cartas `A` con un valor de 1.

```python
>> > higher_card('K', '10')
('K', '10')

>> > higher_card('4', '6')
'6'

>> > higher_card('K', 'A')
'K'
```

### 3. Calcular el valor de un as

Como se mencionó antes, un as puede valer _1 o 11 puntos_.
Los jugadores intentan acercarse lo más posible a un puntaje de 21, sin pasarse (_si se pasa, se dice que se "ha
estallado"_).

Define la función `value_of_ace(<card_one>, <card_two>)` con los parámetros `card_one` y `card_two`, que son un par de
cartas ya en la mano _antes_ de recibir un as.
Tu función deberá decidir si el próximo as tendrá un valor de 1 o de 11, y devolver ese valor.
Recuerda: el valor de la mano con el as debe ser lo más alto posible _sin_ superar los 21.

**Pista**: Si ya tenemos un as en la mano, entonces el valor para el próximo as será 1.

```python
>> > value_of_ace('6', 'K')
1

>> > value_of_ace('7', '3')
11
```

### 4. Determinar una mano "Natural" o "Blackjack"

Si un jugador recibe un as (`A`) y una carta de diez (10, `K`, `Q` o `J`) como sus primeras dos cartas, entonces el
jugador tiene un puntaje de 21.
Esto se conoce como una mano de **blackjack**.

Define la función `is_blackjack(<card_one>, <card_two>)` con los parámetros `card_one` y `card_two`, que son un par de
cartas.
Determina si la mano de dos cartas es un **blackjack**, y devuelve `True` si lo es, `False` en caso contrario.

**Nota**: El _cálculo del puntaje_ se puede hacer de varias maneras. Pero si es posible, nos gustaría que verificases si
hay un as y una carta de diez **_en_** la mano (_o en una posición específica_), en lugar de _sumar_ los valores de la
mano.

```python
>> > is_blackjack('A', 'K')
True

>> > is_blackjack('10', '9')
False
```

### 5. Dividir pares

Si las dos primeras cartas de un jugador tienen el mismo valor, como dos seises, o un `Q` y un `K`, un jugador puede
optar por tratarlas como dos manos separadas.
Esto se conoce como "dividir pares".

Define la función `can_split_pairs(<card_one>, <card_two>)` con los parámetros `card_one` y `card_two`, que son un par
de cartas.
Determina si esta mano de dos cartas puede ser dividida en dos pares.
Si la mano puede ser dividida, devuelve `True`, de lo contrario, devuelve `False`.

```python
>> > can_split_pairs('Q', 'K')
True

>> > can_split_pairs('10', 'A')
False
```

### 6. Duplicar la apuesta

Cuando las dos cartas originales suman 9, 10 u 11 puntos, un jugador puede realizar una apuesta adicional igual a su
apuesta original.
Esto se conoce como "duplicar la apuesta".

Define la función `can_double_down(<card_one>, <card_two>)` con los parámetros `card_one` y `card_two`, que son un par
de cartas.
Determina si la mano de dos cartas puede ser "duplicada", y devuelve `True` si puede, `False` en caso contrario.

```python
>> > can_double_down('A', '9')
True

>> > can_double_down('10', '2')
False
```

[blackjack]: https://bicyclecards.com/how-to-play/blackjack/

[standard_deck]: https://en.wikipedia.org/wiki/Standard_52-card_deck

## Source

### Created by

- @Ticktakto
- @Yabby1997
- @limm-jk
- @OMEGA-Y
- @wnstj2007
- @pranasziaukas
- @bethanyG

### Contributed to by

- @PaulT89