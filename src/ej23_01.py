def pedir_edad() ->int:
    edad_incorreta=True
    
    while edad_incorreta:
     try:
      edad= None
      edad=int(input("Dime tu edad:"))
      
      if edad<0:
          raise ValueError("La edad debe ser un número positivo.")
      if edad==0:
          raise ValueError("La edad debe ser un número positivo mayor que cero.")
      if edad>125:
          raise ValueError("La edad debe ser un Número inferior o igual a 125.")
     except ValueError as e:
        if edad is None:
           print(f"*ERROR* el número introducido no es un entero válido. Intentalo de nuevo.")
        else:
           print(f"*ERROR* {e}. Intentalo de nuevo.")   
     
                 
     return edad


def mostrar_anios_cumplidos(edad: int):
    for i in range(1, edad + 1):
        if i == edad:
            print (i)
        else:
            print(i , end=", ")




def main():
   edad = pedir_edad()
   mostrar_anios_cumplidos(edad)



if __name__=="__main__":
   main()   
