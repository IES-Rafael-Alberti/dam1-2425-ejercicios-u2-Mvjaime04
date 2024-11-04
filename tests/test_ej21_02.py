import pytest
from src.ej21_02 import comprobar_pass

def test_password_correcto():
   
    pass_usuario = "contraseña"
    pass_secreta = "contraseña"
    assert comprobar_pass(pass_usuario, pass_secreta) is True

def test_password_incorrecto():
 
    pass_usuario = "contraseña_incorrecta"
    pass_secreta = "contraseña"
    assert comprobar_pass(pass_usuario, pass_secreta) is False
