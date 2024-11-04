def pedir_pass() -> str:
    return input("Introduzca contraseña: ").lower()

def comprobar_pass(pass_usuario, pass_secreta) -> bool:
    if pass_usuario == pass_secreta:
        return True
    else:
        raise NameError("Incorrect Password!!")  # Lanza excepción si la contraseña es incorrecta

def main():
    pass_secreta = "contraseña"
    
    try:
        pass_usuario = pedir_pass()
        if comprobar_pass(pass_usuario, pass_secreta):
            print("Contraseña correcta")
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()
