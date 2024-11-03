def sumar_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10  
        numero //= 10       
    return suma

def main():
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 0:
        print("Por favor, ingresa un número entero positivo.")
        return
    suma_digitos_resultado = sumar_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {suma_digitos_resultado}")

if __name__ == "__main__":
    main()
