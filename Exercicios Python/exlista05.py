#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

from random import randint
from time import sleep

lista = []
impar = []
par = []
print('Gerando Números')
for i in range(0, 20):
    n = randint(1, 10)
    lista.append(n)
    print(lista[i], end=' ')
    sleep(0.3)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print()
print(f'Lista inteira - {lista}')
print(f'Lista par - {par}')
print(f'lista impar - {impar}')