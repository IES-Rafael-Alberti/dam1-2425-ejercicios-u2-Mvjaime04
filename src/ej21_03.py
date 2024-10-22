def Realiza_division(dividendo,divisor) -> int :

    if divisor == 0 :
        
        print("Error, no es posible dividir por cero.")
    else:
            division = dividendo/divisor
            return division

    
 

def main():
 
    num1 = int(input("Dime cual es el dividendo: "))
    num2 = int(input("dime cual es el divisor: "))

    print(" el resultado de tu division es el siguiente: ")

    resultado = Realiza_division(num1,num2)

    print(resultado)


if __name__=="__main__":
    main()
