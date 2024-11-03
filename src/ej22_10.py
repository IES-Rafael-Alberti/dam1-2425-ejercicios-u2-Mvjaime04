def solicitar_numero():
    return int(input("Introduce un número entero: "))


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def mostrar_resultado(numero, es_primo):
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")


def main():
    numero = solicitar_numero()
    resultado = es_primo(numero)
    mostrar_resultado(numero, resultado)

if __name__ == "__main__" :
    main()
