def leer_numeros_positivos():
    suma_positivos = 0
    while True:
        numero = int(input("Introduce un número entero (0 para terminar): "))
        if numero == 0:
            break
        if numero > 0:
            suma_positivos += numero
    return suma_positivos

def main():
    suma_total_positivos = leer_numeros_positivos()
    print(f"La suma de todos los números positivos ingresados es: {suma_total_positivos}")

if __name__ == "__main__":
    main()
