'''Código para verificação de número divisivel por 5 ou 7'''
from modulo_05_function import multiplo
COUNT = 'Y'
while COUNT == 'Y':
    num = int(input("Insira um número natural: "))
    multiplo(num)
    COUNT = input("Deseja continuar, digite 'Y'. Caso contrário digite qualquer letra:").upper()
