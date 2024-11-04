def pedir_num():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("Error: Debe ingresar un número entero positivo.")
        except ValueError:
            print("Error: Entrada no válida. Debe ingresar un número entero.")

def recopilar_numeros(hasta):
    numeros = []
    for i in reversed(range(0, hasta + 1)):
        numeros.append(str(i))
    
    print(f"Cuenta atrás desde {hasta} hasta 0:", ", ".join(numeros))

def main():
    numero = pedir_num()
    recopilar_numeros(numero)

if __name__ == "__main__":
    main()
