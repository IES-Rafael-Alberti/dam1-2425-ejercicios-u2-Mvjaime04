def mayoria_edad(edad,validez):
    return (f"tienes {edad} años de edad por lo que {validez} ")

def main():
    años=int(input("dime tu edad: "))
    
    valido=años
    if valido>= 18:
     valido="eres mayor de edad"
    else:
     valido="eres menor de edad."

    resultado=mayoria_edad(años,valido)
    print(resultado) 
if __name__=="__main__":
   main()