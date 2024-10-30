print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")
#Practicando funciones
#8- Argumentos arbitrarios de palabras clave, **kwargs
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, 
#agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes del nombre del parámetro:

#Ícono de validado por la comunidad

def my_function(**kid):
    print(" Su apellido es " + kid["lname"])

my_function(fname = "Danna", lname = "Martinez")