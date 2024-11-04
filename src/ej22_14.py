def leer_numeros():
    suma = 0
    while True:
        numero = int(input("Introduce un número entero (0 para terminar): "))
        if numero == 0:
            break
        suma += numero
    return suma

def main():
    suma_total = leer_numeros()
    print(f"La suma de todos los números ingresados es: {suma_total}")

if __name__ == "__main__":
    main()
