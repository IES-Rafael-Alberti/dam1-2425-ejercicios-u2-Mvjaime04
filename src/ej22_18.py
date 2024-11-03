def sumar_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10  # Sumar el último dígito
        numero //= 10        # Eliminar el último dígito
    return suma

def main():
    contador_pares = 0
    
    while True:
        numero = int(input("Introduce un número entero positivo (-1 para terminar): "))
        if numero == -1:
            break
        if numero < 0:
            print("Por favor, ingresa un número entero positivo.")
            continue
        
        suma_digitos_resultado = sumar_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {suma_digitos_resultado}")
        
        if numero % 2 == 0:
            contador_pares += 1
    
    print(f"Se ingresaron {contador_pares} números pares.")

if __name__ == "__main__":
    main()
