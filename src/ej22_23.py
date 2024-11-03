def contar_digitos(titulos):
    conteo_digitos = 0
    for titulo in titulos:
        conteo_digitos += sum(c.isdigit() for c in titulo)
    return conteo_digitos

def main():
    lineas_completas = 0
    
    while True:
        titulos = []
        while True:
            libro = input("Libro: ")
            if libro == "*":
                if titulos:
                    break
                else:
                    print("Fin. Se leyeron 0 líneas completas.")
                    return
            
            if libro == "/":
                if titulos:
                    conteo_digitos = contar_digitos(titulos)
                    print(f"Línea completa. Aparecen {conteo_digitos} dígitos numéricos.")
                    lineas_completas += 1
                    titulos.clear()
            else:
                titulos.append(libro)

        print(f"Fin. Se leyeron {lineas_completas} líneas completas.")

if __name__ == "__main__":
    main()

