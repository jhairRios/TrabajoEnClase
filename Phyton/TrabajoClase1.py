#Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te 
#recomiendo almacenar esas letras en una lista y luego usar algún método propio de string 
#que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que 
#debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas 
#y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se 
#encuentren absolutamente todas las letras es pasar, tanto el texto original como las 
#letras a buscar, a minúsculas.

import os
os.system('cls' if os.name == 'nt' else 'clear')

mensaje = print("Ingrese un texto: ")
mensaje.imput()
mensaje.lower()

print("Ingrese la letra que desa contar: ")
letra = input()
veces = mensaje.count(letra)

print("La letra"+str(letra)+"aparece"+str(veces)+"veces")
