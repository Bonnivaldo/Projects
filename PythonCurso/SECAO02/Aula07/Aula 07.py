nome = 'Cleidson'
idade = 25
altura = 1.9
peso = 83
e_maior = idade > 18
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}.')
print(f'{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))

