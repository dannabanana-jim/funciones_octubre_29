print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")
#Practicando funciones

#13- Argumentos sólo posicionales 
#Puede especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.
#Para especificar que una función solo puede tener argumentos posicionales, agregue , / después de los argumentos:
#Ícono de validado por la comunidad


def my_function(x, /):
    print(x)

my_function(5)
