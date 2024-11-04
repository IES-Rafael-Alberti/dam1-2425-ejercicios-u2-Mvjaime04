def mostrar_menu():
    print("Menú:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")

def comenzar_programa():
    print("Programa iniciado. ¡Bienvenido!")

def imprimir_listado():
    print("Este es el listado que solicitaste.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2 o 3): ")
        
        if opcion == '1':
            comenzar_programa()
        elif opcion == '2':
            imprimir_listado()
        elif opcion == '3':
            print("Finalizando el programa. Adiós.")
            break
        else:
            print("Opción incorrecta. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()
