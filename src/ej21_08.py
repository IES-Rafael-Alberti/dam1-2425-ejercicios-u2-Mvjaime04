def pedir_puntuación() -> float :

    puntos = float(input("Dime tu puntuación adquirida en la empresa: "))
    
    return puntos



def main():

    inaceptable = "Inaceptable"
    
    aceptable = "Aceptable"

    meritorio = "Meritorio"

    if pedir_puntuación() == 0.0 :

        print(f"{inaceptable}, tu sueldo es de 0 euros" )
    elif pedir_puntuación() == 0.4 :

        print(f"{aceptable}, tu sueldo es de {2400 * 0.4} euros")
    elif pedir_puntuación() >= 0.6 :

        print(f"{meritorio}, tu sueldo es de {2400 * pedir_puntuación()} euros")
    else :
        
        print("La puntuación introducida no corresponde a una opción registrada (Las opciones registradas son 0.0, 0.4, 0,6 o superior.)")

if __name__ == "__main__" :
   
    main()