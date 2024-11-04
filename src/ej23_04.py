def pedir_entero():
    try:
        numero = int(input("Ingrese un número entero: "))
        print(f"Número ingresado correctamente: {numero}")
    except ValueError:
        print("La entrada no es correcta")
        raise  
    
def main():
    try:
        pedir_entero()
    except ValueError as e:
        print(f"Excepción capturada: {e}")

if __name__ == "__main__":
    main()
