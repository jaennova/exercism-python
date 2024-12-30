# Mitigación de Meltdown

Bienvenido a la sección de Mitigación de Meltdown en la pista de Python de Exercism.  
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.  
Si te atascas en el ejercicio, revisa `HINTS.md`, pero intenta resolverlo sin usarlos primero. :)

## Introducción

En Python, las declaraciones [`if`][if statement], `elif` (_contracción de 'else if'_) y `else` se usan para [controlar el flujo][control flow tools] de ejecución y tomar decisiones en un programa.  
A diferencia de muchos otros lenguajes de programación, las versiones de Python 3.9 y anteriores no ofrecen una declaración formal de case-switch. En su lugar, se utilizan múltiples declaraciones `elif` para lograr un propósito similar.

Python 3.10 introduce una variante llamada `structural pattern matching`, que se cubrirá por separado en otro concepto.

Las declaraciones condicionales utilizan expresiones que deben resolverse en `True` o `False`, ya sea devolviendo directamente un tipo `bool` o evaluándose como ["truthy" o "falsy"][truth value testing].

```python
x = 10
y = 5

# La comparación '>' devuelve el bool 'True',
# por lo que se imprime el mensaje.
if x > y:
    print("x es mayor que y")
...
>>> x es mayor que y
```

Cuando se combina con `if`, un bloque de código opcional `else` se ejecutará cuando la condición original de `if` evalúe como `False`:

```python
x = 5
y = 10

# La comparación '>' aquí devuelve el bool 'False',
# por lo que se ejecuta el bloque 'else' en lugar del bloque 'if'.
if x > y:
    print("x es mayor que y")
else:
    print("y es mayor que x")
...
>>> y es mayor que x
```

`elif` permite realizar múltiples evaluaciones o ramificaciones:

```python
x = 5
y = 10
z = 20

# La declaración 'elif' permite verificar más condiciones.
if x > y:
    print("x es mayor que y y z")
elif y > z:
    print("y es mayor que x y z")
else:
    print("z es mayor que x y y")
...
>>> z es mayor que x y y
```

[Operaciones booleanas][boolean operations] y [comparaciones][comparisons] pueden combinarse con condicionales para pruebas más complejas:

```python
>>> def fizzbuzz_clasico(numero):
        if numero % 3 == 0 and numero % 5 == 0:
            resultado = 'FizzBuzz!'
        elif numero % 5 == 0:
            resultado = 'Buzz!'
        elif numero % 3 == 0:
            resultado = 'Fizz!'
        else:
            resultado = str(numero)
        
        return resultado

>>> fizzbuzz_clasico(15)
'FizzBuzz!'

>>> fizzbuzz_clasico(13)
'13'
```

[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not  
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons  
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools  
[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement  
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing  

## Instrucciones

En este ejercicio, desarrollaremos un sistema de control simple para un reactor nuclear.

Para que un reactor produzca energía, debe estar en un estado de _criticidad_.  
Si el reactor está en un estado inferior a la criticidad, puede dañarse.  
Si el estado del reactor supera la criticidad, puede sobrecargarse y provocar un meltdown.  
Queremos mitigar las posibilidades de un meltdown y gestionar correctamente el estado del reactor.

Las siguientes tres tareas están relacionadas con escribir código para mantener el estado ideal del reactor.

---

## 1. Verificar la criticidad

Lo primero que debe hacer un sistema de control es verificar si el reactor está equilibrado en criticidad.  
Se dice que un reactor está en criticidad si cumple las siguientes condiciones:

- La temperatura es menor a 800 K.  
- El número de neutrones emitidos por segundo es mayor a 500.  
- El producto de la temperatura y los neutrones emitidos por segundo es menor a 500,000.

Implementa la función `is_criticality_balanced()` que toma como parámetros `temperature` (medida en kelvin) y `neutrons_emitted`, y devuelve `True` si se cumplen las condiciones de criticidad, o `False` en caso contrario.

```python
>>> is_criticality_balanced(750, 600)
True
```

---

## 2. Determinar el rango de eficiencia de salida de energía

Una vez que el reactor ha comenzado a producir energía, se debe determinar su eficiencia.  
La eficiencia puede agruparse en 4 bandas:

1. `green` -> eficiencia del 80% o más,  
2. `orange` -> eficiencia menor al 80% pero al menos del 60%,  
3. `red` -> eficiencia inferior al 60%, pero aún del 30% o más,  
4. `black` -> eficiencia menor al 30%.  

El valor porcentual se puede calcular como `(generated_power/theoretical_max_power)*100`,  
donde `generated_power` = `voltage` * `current`.  

Ten en cuenta que el valor porcentual generalmente no es un número entero, por lo que debes considerar el uso adecuado de las comparaciones `<` y `<=`.

Implementa la función `reactor_efficiency(<voltage>, <current>, <theoretical_max_power>)`, con tres parámetros: `voltage`, `current` y `theoretical_max_power`.  
Esta función debe devolver la banda de eficiencia del reactor: 'green', 'orange', 'red' o 'black'.

```python
>>> reactor_efficiency(200, 50, 15000)
'orange'
```

---

## 3. Mecanismo de seguridad

Tu tarea final implica crear un mecanismo de seguridad para evitar sobrecargas y meltdown.  
Este mecanismo determinará si el reactor está por debajo, en o por encima del umbral crítico ideal.  
La criticidad puede incrementarse, disminuirse o detenerse insertando (o removiendo) barras de control en el reactor.

Implementa la función `fail_safe()`, que toma 3 parámetros: `temperature` (medida en kelvin), `neutrons_produced_per_second` y `threshold`, y devuelve un código de estado para el reactor.

- Si `temperature * neutrons_produced_per_second` < 90% de `threshold`, devuelve el código de estado 'LOW', indicando que deben retirarse barras de control para producir energía.  
- Si el valor de `temperature * neutrons_produced_per_second` está dentro del 10% del `threshold` (ya sea 0-10% menos que el umbral, igual al umbral o 0-10% más que el umbral), el reactor está en _criticidad_, y debe devolverse el código de estado 'NORMAL', indicando que el reactor está en condición óptima y las barras de control están en posición ideal.  
- Si `temperature * neutrons_produced_per_second` no está en los rangos mencionados, el reactor está entrando en meltdown y debe devolverse el código de estado 'DANGER' para apagar el reactor de inmediato.

```python
>>> fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
'DANGER'
```  

---  

## Fuente

### Creado por  
- @sachsom95  
- @BethanyG  

### Contribuciones de  
- @kbuc  