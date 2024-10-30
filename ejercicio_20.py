print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")

# Practicando funciones
# 20 Recursividad
# Python también acepta la recursividad de funciones, lo que significa que una función definida puede llamarse a sí misma.
# La recursividad es un concepto matemático y de programación común. Significa que una función se llama a sí misma.
# Esto tiene la ventaja de que puede recorrer los datos para llegar a un resultado.
# El desarrollador debe tener mucho cuidado con la recursividad, ya que puede ser bastante fácil escribir una función que nunca termina,
# o una que utiliza cantidades excesivas de memoria o potencia del procesador.
# Sin embargo, cuando se escribe correctamente, la recursividad puede ser un enfoque
# de programación muy eficiente y matemáticamente elegante.
# En este ejemplo, tri_recursion() es una función que hemos definido para llamarse a sí misma ("recurse").
# Usamos la variable k como datos, que disminuye (-1) cada vez que recurrimos.
# La recursividad finaliza cuando la condición no es mayor que 0 (es decir, cuando es 0).
# A un nuevo desarrollador le puede llevar algún tiempo descubrir cómo funciona exactamente esto;
# la mejor manera de averiguarlo es probándolo y modificándolo.

# Ejemplo
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nResultados del ejemplo de recursividad")
tri_recursion(6)

"""
Explicación:
Este procedimiento es similar al cálculo del factorial de un número, pero en este caso se trata de una suma.

1. La función `tri_recursion` toma un parámetro `k`.

2. La función verifica si `k` es mayor que 0. Si es así, calcula la suma de `k` y el resultado de llamar a `tri_recursion` con el argumento `k - 1`.
Esto se hace de forma recursiva hasta que `k` se convierta en 0.

3. Si `k` no es mayor que 0, la función establece `result` en 0.

4. La función devuelve el "result".

5. Finalmente, se llama a la función con el argumento `6` y el resultado se imprime en la consola.

Al ejecutar este código, debería generar:
Resultados del ejemplo de recursividad:
1
3
6
10
15
21
El resultado muestra la suma de los números del 6 al 1, impresos en orden descendente.
La primera llamada a `tri_recursion` calcula la suma de 6+5+4+3+2+1, que es 21.
"""