# Currency Exchange

Bienvenido a Currency Exchange en la sección de Python de Exercism.  
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.  
Si te atascas en el ejercicio, revisa `HINTS.md`, pero intenta resolverlo sin usar esos recursos primero. :)

## Introducción

## Números

Python tiene tres tipos de números incorporados: `ints`, `floats` y `complex`. Sin embargo, en este ejercicio solo trabajarás con `ints` y `floats`.

### ints

Los `ints` son números enteros. Por ejemplo: `1234`, `-10`, `20201278`.

Los enteros en Python tienen [precisión arbitraria][arbitrary-precision], lo que significa que el número de dígitos está limitado solo por la memoria disponible del sistema.

### floats

Los `floats` son números que contienen un punto decimal. Por ejemplo: `0.0`, `3.14`, `-9.01`.

Los números en punto flotante generalmente se implementan en Python usando un `double` en C (_15 decimales de precisión_), pero su representación puede variar dependiendo del sistema anfitrión y otros detalles de implementación. Esto puede generar sorpresas al trabajar con floats, pero es "suficiente" para la mayoría de los casos.

Puedes encontrar más detalles y discusiones en los siguientes recursos:

- [Documentación de tipos numéricos en Python][numeric-type-docs]
- [El tutorial de Python][floating point math]
- [Documentación del método `int()`][`int()` built in]
- [Documentación del método `float()`][`float()` built in]
- [0.30000000000000004.com][0.30000000000000004.com]

## Aritmética

Python soporta completamente operaciones aritméticas entre `ints` y `floats`. Convertirá números más pequeños para que coincidan con sus contrapartes más amplias al usar operadores aritméticos binarios (`+`, `-`, `*`, `/`, `//` y `%`). En la división con `/`, `//` devuelve el cociente y `%` el resto.

Python considera a los `ints` más pequeños que los `floats`. Por lo tanto, usar un float en una expresión garantiza que el resultado también será un float. Sin embargo, al hacer divisiones, el resultado siempre será un float, incluso si solo se usan enteros.

```python
# El int se convierte en float aquí, y el tipo de retorno es float.
>>> 3 + 4.0
7.0
>>> 3 * 4.0
12.0
>>> 3 - 2.0
1.0
# La división siempre devuelve un float.
>>> 6 / 2
3.0
>>> 7 / 4
1.75
# Calculando restos.
>>> 7 % 4
3
>>> 2 % 4
2
>>> 12.75 % 3
0.75
```

Si necesitas un resultado entero, puedes usar `//` para truncar el resultado.

```python
>>> 6 // 2
3
>>> 7 // 4
1
```

Para convertir un float en un entero, puedes usar `int()`. Asimismo, para convertir un entero en un float, puedes usar `float()`.

```python
>>> int(6 / 2)
3
>>> float(1 + 2)
3.0
```

[0.30000000000000004.com]: https://0.30000000000000004.com/  
[`float()` built in]: https://docs.python.org/3/library/functions.html#float  
[`int()` built in]: https://docs.python.org/3/library/functions.html#int  
[arbitrary-precision]: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#:~:text=In%20computer%20science%2C%20arbitrary-precision,memory%20of%20the%20host%20system.  
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html  
[numeric-type-docs]: https://docs.python.org/3/library/stdtypes.html#typesnumeric  

## Instrucciones

Tu amigo Chandler planea visitar países exóticos alrededor del mundo. Lamentablemente, sus habilidades matemáticas no son buenas. Está preocupado por ser estafado en los cambios de divisas durante su viaje, así que quiere que desarrolles una calculadora de divisas para él. Aquí están las especificaciones para la aplicación:

## 1. Estimar el valor después del cambio

Crea la función `exchange_money()` con los siguientes parámetros:

1. `budget`: La cantidad de dinero que planeas cambiar.  
2. `exchange_rate`: La cantidad de moneda local equivalente a una unidad de moneda extranjera.

Esta función debe devolver el valor de la moneda cambiada.

**Nota:** Si tu moneda es USD y deseas cambiar USD a EUR con una tasa de cambio de `1.20`, entonces `1.20 USD == 1 EUR`.

```python
>>> exchange_money(127.5, 1.2)
106.25
```

---

### 2. Calcular el cambio restante después de un intercambio

Crea la función `get_change()`, que toma dos parámetros:

1. `budget`: La cantidad de dinero antes del intercambio.
2. `exchanging_value`: La cantidad de dinero que se *toma* del presupuesto para intercambiar.

Esta función debe devolver la cantidad de dinero que *queda* del presupuesto.

```python
>>> get_change(127.5, 120)
7.5
```

---

### 3. Calcular el valor de los billetes

Crea la función `get_value_of_bills()`, que toma dos parámetros:

1. `denomination`: El valor de un solo billete.
2. `number_of_bills`: El número total de billetes.

Esta cabina de cambio solo opera con efectivo en incrementos específicos.  
El total que recibas debe ser divisible por el valor de un billete o unidad, lo que puede dejar un residuo.  
Tu función debe devolver únicamente el valor total de los billetes (_excluyendo los montos fraccionarios_) que la cabina entregaría.  
Desafortunadamente, la cabina se queda con el residuo/cambio como una bonificación adicional.

```python
>>> get_value_of_bills(5, 128)
640
```

---

### 4. Calcular el número de billetes

Crea la función `get_number_of_bills()`, que toma los parámetros `amount` y `denomination`.

Esta función debe devolver el _número de billetes de moneda_ que puedes recibir con la cantidad inicial.  
En otras palabras: ¿Cuántos _billetes completos_ caben en el monto inicial?  
Recuerda: solo puedes recibir _billetes completos_, no fracciones, por lo que debes dividir adecuadamente.  
Efectivamente, estás redondeando hacia _abajo_ al billete entero más cercano.

```python
>>> get_number_of_bills(127.5, 5)
25
```

---

### 5. Calcular el sobrante después de cambiar a billetes

Crea la función `get_leftover_of_bills()`, que toma los parámetros `amount` y `denomination`.

Esta función debe devolver la _cantidad sobrante_ que no puede ser devuelta a partir del monto inicial dado el valor de los billetes.  
Es muy importante saber exactamente cuánto se queda la cabina.

```python
>>> get_leftover_of_bills(127.5, 20)
7.5
```

---

### 6. Calcular el valor después del intercambio

Crea la función `exchangeable_value()`, que toma los parámetros `budget`, `exchange_rate`, `spread` y `denomination`.

El parámetro `spread` es el *porcentaje cobrado* como comisión por el intercambio, escrito como un número entero.  
Debe convertirse a un decimal dividiéndolo entre 100.  
Por ejemplo: Si `1.00 EUR == 1.20 USD` y el *spread* es `10`, la tasa de cambio real será:  
`1.00 EUR == 1.32 USD` porque el 10% de 1.20 es 0.12, y esta tarifa adicional se suma a la tasa de cambio.

Esta función debe devolver el valor máximo de la nueva moneda después de calcular la *tasa de cambio* más el *spread*.  
Recuerda que la *denominación* de la moneda es un número entero y no puede subdividirse.

**Nota:** El valor devuelto debe ser de tipo `int`.

```python
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
>>> exchangeable_value(127.25, 1.20, 10, 5)
95
```

--- 

## Fuente

### Creado por

- @Ticktakto
- @Yabby1997
- @limm-jk
- @OMEGA-Y
- @wnstj2007
- @J08K

### Contribuciones de

- @BethanyG
- @kytrinyx
- @pranasziaukas