def pedir_edad() :
    return int(input("Introduzca su edad: "))

def main() :
    edad = pedir_edad()

    for i in range (1, edad + 1) :
        
        print(i)
if __name__ == "__main__" :
    main()