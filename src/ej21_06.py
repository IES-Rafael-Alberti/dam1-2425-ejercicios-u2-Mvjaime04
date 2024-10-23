def pedir_sexo():
    sexo = input("Dime cual es tu sexo: ").lower()
    
    return sexo

def pedir_nombre(): 
    nombre = input("Dime tu nombre: ").lower()

    return nombre 

def comprobar_sexo(sexo, sexo_hombre, sexo_mujer)-> bool :
    
    if sexo == sexo_hombre or sexo == sexo_mujer:
        return True
    else:
        return False

def comprobar_nombre(nombre) -> bool :
 if nombre < "m":
     return True
 elif nombre > "n":
     return False
 
def main():
    sexo_hombre = "hombre"
    sexo_mujer = "mujer"

    sexo = pedir_sexo()

    nombre = pedir_nombre()

    if comprobar_sexo(sexo,sexo_hombre,sexo_mujer) == True and comprobar_nombre(nombre) == True :
        if sexo== sexo_mujer:
            print( "estas en el grupo A")
        else:
            print("estas en el grupo B")
    elif comprobar_sexo(sexo,sexo_hombre,sexo_mujer) == True and comprobar_nombre(nombre) == False:

        if sexo == sexo_hombre:
            print("stas en el grupo A")
        else:
            print("estas en el grupo B")
    else:
        print("ERROR, introduce bien tus datos de sexo")

if __name__=="__main__":
    main()        
     
