def pedir_respuesta():
    return input("¿Eres vegetariano o no? (s/n): ").lower()

def comprobar_vegetariano():
    respuesta = pedir_respuesta()
    while respuesta not in ("s", "n"):
        print("Introduce una respuesta correcta (s/n)")
        respuesta = pedir_respuesta()
    return respuesta == "s"

def main():
    ingredientes_vegetarianos = ["pimiento", "tofu"]
    ingredientes_novege = ["peperoni", "jamón", "salmón"]

    if comprobar_vegetariano():
        print("Tus ingredientes disponibles son pimiento y tofu (el tomate y la mozzarella están incluidas en todas las pizzas).")
        vege = input("Introduzca uno de los ingredientes (pimiento-tofu): ").lower()
        
        if vege in ingredientes_vegetarianos:
            print(f"Tu pizza es vegetariana y contiene {vege}, tomate y mozzarella.")
        else:
            print("ERROR, introduzca uno de los ingredientes propuestos.")
    else:
        print("Tus ingredientes disponibles son peperoni, jamón y salmón (el tomate y la mozzarella están incluidos en todas las pizzas).")
        no_vege = input("Introduzca uno de los ingredientes (peperoni, jamón, salmón): ").lower()

        if no_vege in ingredientes_novege:
            print(f"Tu pizza no es vegetariana y contiene {no_vege}, tomate y mozzarella.")
        else:
            print("ERROR, introduzca uno de los ingredientes propuestos.")

if __name__ == "__main__":
    main()