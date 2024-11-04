def mostrar_impares(n):
    impares = [str(i) for i in range(1, n + 1) if i % 2 != 0]
    print(", ".join(impares))

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero > 0:
            mostrar_impares(numero)
        else:
            print("Error: Debe ingresar un número entero positivo.")
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()
