import os
os.system ("cls")

def invertir_array(array):
    array_invertido = []
    
    for i in range(len(array) - 1, -1, -1):
        array_invertido.append(array[i])
    return array_invertido
    
print("Bienvenido 😁👌😝")
print("🫡este programa te permirira ingresar elementos y los devolvera invertidos 💫")

n= int(input("🧮ingresa la cantidad de elementos del array(lista): "))

array = []

for i in range(n):
    valor = input(f"➡️ Ingresa el elemento {i + 1}: ")
    array.append(valor)
    
array_intertido = invertir_array(array)

print("\n👌 Array original:", array)
print(f"🎯 Array invertido: {array_intertido}")
print("\n✅ El proceso ha sido completado con exito 😘😝")

    
    

    
    
    



