print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")
#Practicando funciones
#19 Combine solo posicional y solo palabras clave
#Puede combinar los dos tipos de argumentos en la misma función.
#Cualquier argumento antes de / es solo posicional y cualquier argumento después de * es solo de palabra clave.
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(1, 1, c = 1, d = 1)
