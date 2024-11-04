def eco():
    while True:
        texto = input("Escribe algo: ")
        if texto.lower() == "salir":
            print("Programa terminado.")
            break
        print(texto)

def main():
    eco()

if __name__ == "__main__":
    main()