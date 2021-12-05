nome = 'Cleidson'
idade = 27
altura = 1.71
peso = 56
ano_atual = '2021'
ano_nasc = int(ano_atual) - idade
#ano_nasc = ano_atual - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
print('O IMC de {} é {:.2f}'.format(nome, imc))
print(nome,'nasceu em',ano_nasc)
