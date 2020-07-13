from random import randint
from collections import Counter
from operator import itemgetter
from time import sleep

nvoto = int(input('Digite o número de votos: '))
print(f'O sistema irá simular usando randint {nvoto} votos', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
votos = []
for i in range(0, nvoto):
    votos.append(randint(1, 23))

print()
print(f'Foram computados {len(votos)} votos')
print()
sleep(2)
a = Counter(votos)
print('-'*30)
print(f'{"Jogador":<10}{"Votos":^12}{"%":>5}')
print('-'*30)

for k, v in a.items():
    print(f'{k:<10}{v:^12}{v/len(votos)*100:>5.2f}%')

maior = max(a.items(), key=itemgetter(1))
print(f'O vencedor foi o jogador {maior[0]}, com {maior[1]} votos')
