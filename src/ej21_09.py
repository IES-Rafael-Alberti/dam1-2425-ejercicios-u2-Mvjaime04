def pedir_edad():
    
    edad = int(input("Introduce tu edad: "))
    
    return edad 

def main():

    if pedir_edad() >0 and pedir_edad() < 4 :
        
        print("Tu entrada es gratuita, pase dentro :).")
    elif pedir_edad() >= 4 and pedir_edad() <= 18 :

        print("Su precio por entrada es de 5 euros.")
    elif pedir_edad() > 18 :
        
        print("Su precio por entrada es de 10 euros.")
    elif pedir_edad() <= 0 or pedir_edad() > 125 :

        print("La edad introducida no es correcta, porfavor introduzca una edad real.")        

if __name__ == "__main__":
    main()