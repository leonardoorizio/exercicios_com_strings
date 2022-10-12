'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''

def data_de_nscimento():

    meses_do_ano = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    dia = input('Digite o dia que você nasceu:')
    mes = input('Digite o mês que você nasceu:')
    ano = input('Digite o ano que você nasceu:')

    print('\nVocê nasceu em ' + dia + ' de ' + meses_do_ano[int(mes) - 1] + ' de ' + ano + '.')

data_de_nscimento()