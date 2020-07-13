#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
from random import randint
from collections import Counter
from time import sleep
from operator import itemgetter

print('-'*30)
print('PROBABILIDADE DE UM DADO')
print('-'*30)
print('Jogando o dado 100 vezes.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')

dados = []
for i in range(0, 100):
    dados.append(randint(1, 6))
dados.sort()
cont = Counter(dados)
print(cont)
for k, v in cont.items():
    print(f'O nº{k} apareceu {v} vezes')
