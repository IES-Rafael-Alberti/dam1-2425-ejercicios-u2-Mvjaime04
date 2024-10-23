def identificador_par_impar(numero) :
    modulo= numero % 2
    if modulo == 0:
        print("El número introducido es par")
    else:
        print("El número introducido es impar")

def main():
    num = int(input("Introduce un número: "))
    identificador_par_impar(num)
if __name__=="__main__":
    main()