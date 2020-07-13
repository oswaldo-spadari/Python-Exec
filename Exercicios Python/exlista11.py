# Altere o programa 10 anterior, intercalando 3 vetores de 10 elementos cada.
from random import randint

lista1 = []
lista2 = []
lista3 = []
lista4 = []
for c in range(0, 10):
    lista1.append(randint(0, 30))
    lista2.append(randint(0, 30))
    lista3.append(randint(0, 30))
    lista4.append(lista1[c])
    lista4.append(lista2[c])
    lista4.append(lista3[c])
print(f'lista1 = {lista1}')
print(f'lista2 = {lista2}')
print(f'lista3 = {lista3}')
print(f'lista4 = {lista4}')
