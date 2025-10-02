import os 
os.system("cls")
import random

print("Bienvenido a este programa,identifica numeros 'camaleon' 🦎 ")
cantidad_de_numeros = int(input("¿Que cantidad de numeros desea validar? ej: 1, 2, 3 o mas..."))


def es_camaleon(num):
    num_str = str(num)  
    suma_digitos = sum(int(digito) for digito in num_str)  

    suma_par =suma_digitos % 2 == 0
    
    num_invertido = int(num_str[::-1])
    divisible_por_3 = num_invertido % 3 == 0
    return suma_par and divisible_por_3

for _ in range(cantidad_de_numeros):
    numero = random.randint(100, 99999)  
    print(f"\nEl número aleatorio es: {numero}")

    
    if es_camaleon(numero):
        print(f"{numero} es un número camaleón 🦎")
    else:
        print(f"{numero} NO es un número camaleón 😔")

    

    
    
    
    