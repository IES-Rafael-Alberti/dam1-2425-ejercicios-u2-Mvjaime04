def contar_digitos(numero):
    pares = 0
    impares = 0
    
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    
    return pares, impares

def main():
    total_pares = 0
    total_impares = 0
    
    while True:
        numero = int(input("Introduce un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        if numero < 0:
            print("Por favor, ingresa solo números enteros positivos.")
            continue
        
        pares, impares = contar_digitos(numero)
        print(f"El número {numero} tiene {pares} dígitos pares y {impares} dígitos impares.")
        
        total_pares += pares
        total_impares += impares
    
    print(f"Total de dígitos pares leídos: {total_pares}")
    print(f"Total de dígitos impares leídos: {total_impares}")

if __name__ == "__main__":
    main()
