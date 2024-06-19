# import os
# os.system('cls' if os.name == 'nt' else 'clear')


# Saludo="Hola_Mundo"


# #print(Saludo.rindex('a'))

# try:
#     print(Saludo.index('a'))
# except:
#     print("No se encontro")
    
#     print (Saludo[1:3])
    
#     print(Saludo[2:6])
#     print(Saludo[3:4])

mensaje = "Hola 12345"
numero = "12345"
dcimal = "12345.555"
mensaje2 = "Hola mundo"

print(mensaje.isdigit())
print(numero.isdigit())
print (dcimal.isdigit())

print(mensaje.isnumeric())
print(numero.isnumeric())
print(dcimal.isnumeric())

print(mensaje.isdecimal())
print(numero.isdecimal())
print(dcimal.isdecimal())

print (mensaje.isalnum())
print(mensaje2.isalnum())

mensaje3 = "Hola mundo"
print(mensaje3.replace("Hola","Adios")) 
nombre = "Edson*jhair*Rios*Coto*"
print(nombre.split("*"))
print(nombre.replace("*"," "))