def leer_numeros_positivos():
    mayor_numero = None
    while True:
        numero = int(input("Introduce un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        if numero > 0:
            if mayor_numero is None or numero > mayor_numero:
                mayor_numero = numero
    return mayor_numero

def main():
    mayor = leer_numeros_positivos()
    if mayor is not None:
        print(f"El mayor número ingresado es: {mayor}")
    else:
        print("No se ingresaron números positivos.")

if __name__ == "__main__":
    main()
