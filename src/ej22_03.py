def pedir_numero():
    
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("ERROR, introduce un número entero positivo.")
        except ValueError:
            print("ERROR,introduce un número entero.")

def mostrar_impares(hasta):

    impares = []
    
    for i in range(1, hasta + 1):
        if i % 2 != 0:  
            impares.append(str(i))  

    
    print("Números impares desde 1 hasta", hasta, ":", ", ".join(impares))

def main():
    numero = pedir_numero()
    mostrar_impares(numero)


if __name__ == "__main__":
    main()
