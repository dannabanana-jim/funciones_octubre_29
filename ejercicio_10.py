print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")
#Practicando funciones
#10- Pasar una lista como argumento
#Puede enviar cualquier tipo de argumento de datos a una función (cadena, número, lista, diccionario, etc.)
#y será tratado como el mismo tipo de datos dentro de la función.

#P.ej. Si envía una Lista como argumento, seguirá siendo una Lista cuando llegue a la función:

def my_function(food):
    for x in food:
        print(x)

fruits = ["Cereza", "banana", "Manzana"]

my_function(fruits)
