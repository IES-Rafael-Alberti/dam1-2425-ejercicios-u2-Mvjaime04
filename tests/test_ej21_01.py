import pytest
from src.ej21_01 import mayoria_edad


def test_mayoria_edad_mayor():
  
    edad = 20
    validez = "eres mayor de edad"
    resultado = mayoria_edad(edad, validez)
    assert resultado == "tienes 20 años de edad por lo que eres mayor de edad "

def test_mayoria_edad_menor():
   
    edad = 15
    validez = "eres menor de edad."
    resultado = mayoria_edad(edad, validez)
    assert resultado == "tienes 15 años de edad por lo que eres menor de edad. "

