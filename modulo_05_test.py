'''Teste para validação do código do Modulo 1'''
import pytest

from modulo_05_function import multiplo

class Test:
    def setup_method(self):
        pass
    
    def test_mult_5(self):
        resultado1 = multiplo(15)
        assert resultado1 == (None,"Fizz")

    def test_mult_7(self):
        resultado2 = multiplo(49)
        assert resultado2 == (None,"Buzz")

    def test_mult_both(self):
        resultado3 = multiplo(35)
        assert resultado3 == (None,"FizzBuzz")
        
    def test_multh_null(self):
        resultado4 = multiplo(17)
        assert resultado4 == (None,"Miss")
