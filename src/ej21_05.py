def pedir_edad():
    edad = None
    try:
        edad = int(input("dime que edad tienes: "))
    except ValueError:
        print("ERROR")

    return edad

def pedir_ingresos():
    ingresos=None
    try:
        ingresos = float(input("Dime cuales son tus ingresos mensuales: "))
    except ValueError:
        print("ERROR")

    return ingresos

def comprobar_datos(edad: int ,ingreso: float) -> bool :
    
    if  edad > 16 and ingreso >= 1000 :
        return True
    else :
        return False

def main():
    
    edad = pedir_edad()
    
    if edad != None:
        ingresos = pedir_ingresos()

        if ingresos != None:

            if comprobar_datos(edad,ingresos) == True:

                print("de acuerdo con sus datos usted debe tributar")
            else:

                print("para poder tributar deber ser mayor de 16 años y tener unos ingresos mayores o iguales a 1000 €")



if __name__=="__main__":
    main()    