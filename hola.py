# Definir una cadena
from cgitb import text


texto = "precio = 10 AND precio < 12"

# Verificar si la cadena "otro" está en el texto
if "precio" in texto:
    print("La cadena 'precio' fue encontrada.")
    texto = texto.replace("precio", '10')
    print(texto)
else:
    print("La cadena 'otro' no fue encontrada.")