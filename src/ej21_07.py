def pedir_renta():
    renta = int(input("dime tu renta anual: "))
    return renta

def main():
    renta = pedir_renta()

    if renta < 10000:
        print("Tu renta anual tiene tramo impositivo de un 5%.")
    elif renta >= 10000 and renta <20000:
        print("Tu renta anual tiene un tramo impositivo de un 15%.")
    elif renta >= 20000 and renta < 35000 :
        print("tu renta anual tien un tramo impositivo de un 20%.")
    elif renta >= 35000 and renta < 60000:
        print("tu renta anual tiene un tramo impositivo de un 30%.")
    else:
        print("tu renta anual tiene un tramo impositivo de un 45%.")
if __name__=="__main__":
    main()
    