def calcular_inversion_anual(amount, interest, years):

    print("\nCapital obtenido cada año:")
    for year in range(1, years + 1):
        amount *= 1 + interest / 100
        print(f"Año {year}: {amount:.2f}€")

def main():
    
    amount = float(input("Introduce la cantidad a invertir: "))
    interest = float(input("Introduce el interés anual (%): "))
    years = int(input("Introduce el número de años de la inversión: "))
    
   
    calcular_inversion_anual(amount, interest, years)

if __name__ == "__main__":
    main()
