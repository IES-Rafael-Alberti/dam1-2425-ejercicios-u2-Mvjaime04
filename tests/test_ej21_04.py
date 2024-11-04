import pytest
from src.ej21_04 import identificador_par_impar

def test_identificador_par():
    
    numero = 4
    identificador_par_impar(numero)

    assert "El número introducido es par" 

def test_identificador_impar():
    
    numero = 3
    identificador_par_impar(numero)
    
    assert "El número introducido es impar" 
