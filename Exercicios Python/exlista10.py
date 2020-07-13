#Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
# compostos pelos elementos intercalados dos dois outros vetores.
from random import randint

lista1=[]
lista2=[]
lista3=[]

for c in range(0, 10):
    lista1.append(randint(1, 20))
    lista2.append(randint(1, 20))

for c in range(0, 10):
    l1 = lista1[c]
    l2 = lista2[c]
    lista3.append(l1)
    lista3.append(l2)

print(f'lista1 = {lista1}')
print(f'lista2 = {lista2}')

print(f'{lista3}')
