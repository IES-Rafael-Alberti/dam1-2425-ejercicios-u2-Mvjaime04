def pedir_num() :

    while True:
        try :
            num = int(input(" Introduzca un número: "))
            if num > 0 :
                return num
            else :
                print("ERROR,introduzca un número entero positivo.")
        except ValueError :
            print("ERROR, introduzca un numero entero.")

def recopilar_numeros (hasta) :

    numeros= []

    for i in reversed(range(0, hasta)) :

        numeros.append(str(i))
    
    print(f"Cuenta atrás desde {hasta} hasta 0",":", ", ".join(numeros))

def main():
    numero= pedir_num()

    recopilar_numeros(numero)

if __name__ == "__main__" :
    main()
         

    
