
import os
os.system('cls' if os.name == 'nt' else 'clear')

Programacion = {"Nombre: Jorge Arturo Vallecillo Espinoza" "---Edad:": 18,
                "Nombre: Lucas Rodrigo Bautista Juarez" "------Edad:": 18,
                "Nombre: Jose David Mejia Mendoza" "-----------Edad:": 31,
                "Nombre: Kennet Andersson Martinez Varela" "---Edad:": 21,
                "Nombre: Tomy José Montúfar Zuniga" "----------Edad:": 19,
                "Nombre: Ángel Antonio Pérez Rodríguez" "------Edad:": 18,
                "Nombre: José Eduardo Sabillón Hurtado" "------Edad:": 19,
                "Nombre: Diany Lizbeth Enamorado Fernández " "-Edad:": 19,
                "Nombre: Anderson Jair Garcia Menjivar" "------Edad:": 19,
                "Nombre: Iliana Liceth Zuniga Enamorado" "-----Edad:": 18,
                "Nombre: Derick Dair Muñoz Iraheta" "----------Edad:": 20,
                "Nombre: Norman Bú" "--------------------------Edad:": 25,
                "Nombre: Arnold Stanly Ford" "-----------------Edad:": 18,
                "Nombre: Walter Eduardo Rapalo Smith" "--------Edad:": 20,
                "Nombre: Edson Jhair Ríos coto" "--------------Edad:": 26
                }

for key in Programacion:
    print(f"{key} : {Programacion[key]}")