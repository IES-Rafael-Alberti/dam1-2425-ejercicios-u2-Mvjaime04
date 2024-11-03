def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    cantidad_primos = 0
    
    while True:
        numero = int(input("Ingresa un número mayor que 1 (0 para terminar): "))
        if numero == 0:
            break
        if numero > 1:
            if es_primo(numero):
                cantidad_primos += 1
        else:
            print("Por favor, ingresa un número mayor que 1.")

    print(f"Cantidad de números primos ingresados: {cantidad_primos}")

if __name__ == "__main__":
    main()
