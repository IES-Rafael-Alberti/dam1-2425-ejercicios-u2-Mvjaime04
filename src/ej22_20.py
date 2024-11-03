def buscar_letra(frase, letra):
    for i in range(len(frase)):
        if frase[i] == letra:
            print(f"La letra '{letra}' se encontró en la posición {i}.")
            return
        else:
            print(f"No hay coincidencia en la posición {i}.")
    print(f"La letra '{letra}' no se encontró en la frase.")

def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra a buscar: ")
    
    if len(letra) != 1:
        print("Por favor, ingresa solo una letra.")
        return
    
    buscar_letra(frase, letra)

if __name__ == "__main__":
    main()
