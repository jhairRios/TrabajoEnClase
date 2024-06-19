import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_diccionario = {"curso":"Python TOTAL","clase":"Diccionarios"}
mi_diccionario["recursos"] = ["notas", "ejercicios","examenes","practicas"]
print(mi_diccionario)
print(mi_diccionario["recursos"][0]) 
