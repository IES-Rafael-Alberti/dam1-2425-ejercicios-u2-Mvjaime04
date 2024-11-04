import pytest

from src.ej22_09 import  comprobar_pass  
def test_comprobar_pass_correcta():
    pass_secreta = "contraseña"
    assert comprobar_pass("contraseña", pass_secreta) == True

def test_comprobar_pass_incorrecta():
    pass_secreta = "contraseña"
    assert comprobar_pass("incorrecta", pass_secreta) == False


