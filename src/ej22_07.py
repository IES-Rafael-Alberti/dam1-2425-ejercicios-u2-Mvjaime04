def mostrar_tablas():
  
    for i in range(1, 11):
        print(f"\nTabla de multiplicar del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

def main():
    mostrar_tablas()


if __name__ == "__main__":
    main()
