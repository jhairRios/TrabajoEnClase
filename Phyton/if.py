import os
os.system('cls' if os.name == 'nt' else 'clear')

edad = int(input("Ingresa tu edad: "))
if edad >= 21:
    print("eres mayor de edad")
elif edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")