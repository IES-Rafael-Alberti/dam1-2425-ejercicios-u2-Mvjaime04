def solicitar_palabra():
    return input("Introduce una palabra: ")

def mostrar_letras_invertidas(palabra):
    for letra in palabra[::-1]:
        print(letra)

def main():
    palabra = solicitar_palabra()
    mostrar_letras_invertidas(palabra)

main()
