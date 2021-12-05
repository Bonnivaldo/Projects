"""
Entrada de dados
"""


nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
nasc = 2021 - int(idade)
print(f'O usuário digitou {idade} e o tipo da variável é {type(idade)}')
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {nasc}')