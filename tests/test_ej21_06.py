import pytest
from src.ej21_06 import comprobar_sexo, comprobar_nombre

def test_comprobar_sexo_hombre():
   
    sexo = "hombre"
    sexo_hombre = "hombre"
    sexo_mujer = "mujer"
    assert comprobar_sexo(sexo, sexo_hombre, sexo_mujer) is True

def test_comprobar_sexo_mujer():
    
    sexo = "mujer"
    sexo_hombre = "hombre"
    sexo_mujer = "mujer"
    assert comprobar_sexo(sexo, sexo_hombre, sexo_mujer) is True

def test_comprobar_sexo_otro():
    
    sexo = "otro"
    sexo_hombre = "hombre"
    sexo_mujer = "mujer"
    assert comprobar_sexo(sexo, sexo_hombre, sexo_mujer) is False

def test_comprobar_nombre_menor_m():
   
    nombre = "ana"
    assert comprobar_nombre(nombre) is True

def test_comprobar_nombre_mayor_n():
    
    nombre = "zara"
    assert comprobar_nombre(nombre) is False


