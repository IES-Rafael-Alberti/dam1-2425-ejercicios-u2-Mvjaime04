import pytest
from src.ej21_03 import Realiza_division

def test_division_valida():
    
    dividendo = 10
    divisor = 2
    resultado = Realiza_division(dividendo, divisor)
    assert resultado == 5

def test_division_por_cero():
    
    dividendo = 10
    divisor = 0
    resultado = Realiza_division(dividendo, divisor)
    
 
    assert resultado is None

   
    
    assert "Error, no es posible dividir por cero." 
