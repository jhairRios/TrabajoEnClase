import os
os.system('cls' if os.name == 'nt' else 'clear')

print("ingrese una palabra: ")
palindromo = input()

palindromo = palindromo.lower()
palabra_Invertida = palindromo[::-1]

if palindromo == palabra_Invertida:
    print("Es palindromo")
else:
    print("No es palindromo")