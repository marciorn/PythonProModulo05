"""Módulo para verificação de númermos divisíveis por 5 ou 7"""
def multiplo(num):
    '''Verificações para verificar se o numero é divisivel por 5 ou 7'''
    if num % 5 == 0 and num % 7 == 0:
        return print("FizzBuzz"), str("FizzBuzz")
    if num % 5 == 0:
        return print("Fizz"), str("Fizz")
    if num % 7 == 0:
        return print("Buzz"), str("Buzz")
    return print("Miss"), str("Miss")
