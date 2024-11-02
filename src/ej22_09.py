def pedir_pass() -> str:

    return input("Introduzca contraseña: ").lower()

def comprobar_pass(pass_usuario: str, pass_secreta: str) -> bool:

    return pass_usuario == pass_secreta

def main():
    pass_secreta = "contraseña"  

    while True:
        pass_usuario = pedir_pass()
        
        if comprobar_pass(pass_usuario, pass_secreta):
            print("Contraseña correcta")
            break
        else:
            print("ERROR, vuelve a introducir la contraseña")

if __name__ == "__main__":
    main()
