cantidad = 0
precio = 10
total = 0
print(f"TIENTA DE PELOTAS")
print("Ingrese la cantidad de pelotas: ")
cantidad = int(input())

if (cantidad >= 10):
    total = cantidad * precio
    Total = total - (total * 0.20)  
if cantidad >= 1000:
     Total = total - (total * 0.50)  
print("obtienes un 50 de descuento")
print("El total es: ", total)