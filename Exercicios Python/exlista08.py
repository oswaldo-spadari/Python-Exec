# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
from random import uniform, randint

pessoa = {}
galera = []

for i in range(0, 5):
    pessoa['idade'] = randint(5, 20)
    pessoa['tamanho'] = round(uniform(1, 2), 2)
    galera.append(pessoa.copy())
print(galera)
galera.reverse()
print(galera)
