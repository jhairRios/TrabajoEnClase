
import os
os.system('cls' if os.name == 'nt' else 'clear')

#imprimir 10 valores con un ciclo while
i = 1
while i <= 10:
    print(i)
    i += 1

print("ciclo contrilado por vanderin ")
while True:
    entrada = input("Ingrese s para salir:")
    if entrada == "s":
        break   
    print("ciclo controlado por vanderin 2")
    bandera = "x"
    while bandera != 's':
        bandera = input("Ingrese s para salir:")
         