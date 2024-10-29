import random
import math

contador = 0
max_aciertos = 0
numeros = 0

def numAleatorio() -> int:
    global numeros
    return random.randint(0, numeros)

def comprobarAleatorio(numA: int, numB: int) -> bool:
    if numA == numB:
        return True
    else:
        return False

def diferencia(numA: int, numB:int) -> int:

    diferen = abs(numA - numB)
    pista = ''
    
    if diferen > 75:
        pista = "Te congelas"
    elif diferen > 50:
        pista = "Un poquito de fresco"
    elif diferen > 30:
        pista = "Templadito"
    elif diferen > 20:
        pista = "Empieza a hacer calor"
    elif diferen > 10:
        pista = "Hace calorcillo"
    elif diferen > 5:
        pista = "TE QUEMAS"
    elif diferen >= 0:
        pista = "TE ESTÁS QUEMANDO"
    return pista
  

def posi(numA: int, numB: int) -> bool:

    if numA > numB:
        return False
    elif numA < numB:
        return True

def pedirNumero() -> int:

    global numeros

    num = int(input(f'Introduce un número: '))
    comprobarNum(num)
    while num not in range(0, numeros + 1):
        print(f'*ERROR* El número introducido debe estar entre 0 y {numeros}')
        num = int(input(f'Introduce un número: '))
    else:
        return num
    
def comprobarNum(num: int) -> int:
        return num

def final(numAdivinar: int):

    numUsuario = pedirNumero()
    comprobacion = comprobarAleatorio(numUsuario, numAdivinar)
    global contador
    global max_aciertos
    
    if comprobacion is False:  

        while contador < (max_aciertos - 1):
            diferen = diferencia(numUsuario, numAdivinar)

            pos = posi(numUsuario, numAdivinar)
            if pos == True:
                pos2 = 'está en mayor posición'
            elif pos == False:
                pos2 = 'está en menor posición'
            contador += 1
            print(f'{diferen} y {pos2}')
            print(f'Intento: {contador + 1}')
            final(numAdivinar)

        else: 
            print('Mala suerte, te quedaste sin intentos :(.')
            print(f'El número a adivinar era {numAdivinar}')
            intentar()
    else:
        print('¡Felicidades! :)')
        print('El número era correcto')
        intentar()
    
def intentar():
    print(f'¿Quieres volver a jugar?')
    print(f'(1 = Sí, 2 = No)')
    n = int(input(""))
    global contador 

    if n == 1:
        contador = 0
        main()
    if n == 2:
        print(f'Hasta luego')
        exit()

def dificultad():
    print(f'¿En qué modo quieres jugar?')
    var = input('(Facil, Normal, Dificil): ')

    global max_aciertos
    global numeros
    
    var = var.title()

    if var == 'Facil':
        max_aciertos = 10
        numeros = 100
    elif var == 'Normal':
        max_aciertos = 5
        numeros = 100
    elif var == 'Dificil':
        max_aciertos = 10
        numeros = 1000
    else:
        print('No reconozco esa dificultad')
        dificultad()

def main():
    global numeros
    dificultad()
    print(f'Bienvenido, solo tienes {max_aciertos} intentos para averiguar el número, suerte.')
    print(f'Intento: 1')
    numAdivinar = numAleatorio()
    final(numAdivinar)

if _name_ == '_main_':
    main()