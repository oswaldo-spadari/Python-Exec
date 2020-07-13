# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
for i in range(1, 11):
    lista.append(float(input(f'Digite o {i}º número: ')))
lista.sort(reverse=True)
print(lista)

