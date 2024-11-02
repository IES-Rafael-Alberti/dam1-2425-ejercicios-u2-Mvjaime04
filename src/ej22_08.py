def pedir_numero():

    return int(input("Introduce la altura del triángulo: "))

def mostrar_triangulo(altura):
  
    for i in range(1, altura + 1):

        fila = [str(num) for num in range(2 * i - 1, 0, -2)]
        print(" ".join(fila))

def main():
    altura = pedir_numero()  
    mostrar_triangulo(altura)  


if __name__ == "__main__":
    main()
