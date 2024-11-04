def main():
    frase = input("Ingresa una frase: ")
    palabras = frase.split()
    
    if not palabras:
        print("No se ingresaron palabras.")
        return
    
    palabra_mas_larga = max(palabras, key=len)
    cantidad_palabras = len(palabras)
    
    print(f"La palabra más larga es: '{palabra_mas_larga}'")
    print(f"Cantidad de palabras: {cantidad_palabras}")

if __name__ == "__main__":
    main()
