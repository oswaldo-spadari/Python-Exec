# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
from random import randint

boletim = []
alunos = {}
notas = []
total = 0

for i in range(1, 11):
    alunos['nome'] = f'aluno{i}'
    notas.clear()
    for c in range(1, 5):
        notas.append(randint(0, 10))
        alunos['notas'] = notas.copy()
        alunos['media'] = sum(notas) / len(notas)
    boletim.append(alunos.copy())

for a in boletim:
    print(a)
    if a['media'] >= 7:
        total += 1

print(f'O total de alunos com média maior ou igual a 7 é de {total} alunos')
