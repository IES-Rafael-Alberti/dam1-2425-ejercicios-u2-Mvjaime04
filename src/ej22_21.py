def calcular_total(montos):
    total = sum(montos)
    if total > 1000:
        total *= 0.9  
    return total

def main():
    montos = []
    
    while True:
        try:
            monto = float(input("Introduce el monto de la compra (0 para terminar): "))
            if monto == 0:
                break
            elif monto < 0:
                print("Monto negativo, por favor ingresa un monto válido.")
                continue
            
            montos.append(monto)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    total_a_pagar = calcular_total(montos)
    print(f"El total a pagar es: {total_a_pagar:.2f}€")

if __name__ == "__main__":
    main()
