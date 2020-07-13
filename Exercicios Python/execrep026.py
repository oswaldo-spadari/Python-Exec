# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
#
# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

c1 = c2 = c3 = 0
while True:
    voto = int(input('Em qual candidato deseja votar? [1], [2] ou [3] '))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    cont = str(input('Deseja continuar votando? [S/N]')).upper().strip()
    if cont == 'N':
        break

print(f' C1 teve {c1} votos, C2 teve {c2} votos e C3 teve {c3} votos')
