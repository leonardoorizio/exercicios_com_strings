'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo
comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

def comparando_string():

    string1 = input('Entre com a 1º string:')
    string2 = input('Entre com a 2º string:')

    tamanho1 = len(string1)
    print(f'\nTamanho de "{string1}": {tamanho1}')
    tamanho2 = len(string2)
    print(f'Tamanho de "{string2}": {tamanho2}')

    if string1 == string2:
        print('\nAs duas strings são de tamanhos iguais.')
        print('\nAs duas strings possuem conteúdo igual.')
    else:
        print('\nAs duas strings são de tamanhos diferentes.')
        print('\nAs duas strings não possuem conteúdo igual.')

comparando_string()