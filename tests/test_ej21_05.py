import pytest
from src.ej21_05 import comprobar_datos

def test_comprobar_datos_cumple_condiciones():
 
    edad = 18
    ingreso = 1200.0
    assert comprobar_datos(edad, ingreso) is True

def test_comprobar_datos_no_cumple_edad():
   
    edad = 15
    ingreso = 1500.0
    assert comprobar_datos(edad, ingreso) is False

def test_comprobar_datos_no_cumple_ingreso():
   
    edad = 20
    ingreso = 900.0
    assert comprobar_datos(edad, ingreso) is False

def test_comprobar_datos_no_cumple_ambos():
  
    edad = 15
    ingreso = 500.0
    assert comprobar_datos(edad, ingreso) is False
