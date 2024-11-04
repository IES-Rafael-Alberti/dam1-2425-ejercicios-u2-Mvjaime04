def solicitar_frase():
    return input("Introduce una frase: ")

def solicitar_letra():
    return input("Introduce una letra: ")

def contar_letra(frase, letra):
    return frase.count(letra)

def mostrar_resultado(letra, contador):
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")

def main():
    frase = solicitar_frase()
    letra = solicitar_letra()
    contador = contar_letra(frase, letra)
    mostrar_resultado(letra, contador)

if __name__ == "__main__" :
    main()
