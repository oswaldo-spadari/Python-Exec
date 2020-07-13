# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
from random import randint

lista = []
for c in range(0, 5):
    lista.append(randint(0, 10))

print(lista)
print(f'a soma dos numeros da lista é: {sum(lista)}')
multi = 1
for i in lista:
    multi *= i
print(f'a multiplicação de todos os itens da lista é: {multi}')
