import os
os.system('cls' if os.name == 'nt' else 'clear')

lista_1 = ["C","C++","Python","Java"]
lista_2 = ["PHP","SQL","Visual Basic"]
lista_3 = lista_1 + lista_2
lista_4 = ["d", "a", "c", "b", "e"]
lista_5 = [5,4,7,1,9]

print(lista_1[0:2],lista_2[0:2])
print (lista_3)

lista_6 = lista_1 + lista_5

print(lista_6)

lista_7 = [True , False]

print(lista_7)

lista_5.append  (True)
print(lista_5)

lista_5.pop (0)
print(lista_5)

lista_7.sort()
print(lista_7)
