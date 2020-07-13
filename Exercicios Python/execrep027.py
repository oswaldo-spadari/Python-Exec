# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

from random import randint
print()
print('*' * 30)
print('Quem irá lavar a louça????')
print('*' * 30)
while True:
    Vinicius = randint(1, 10)
    Melissa = randint(1, 10)
    Oswaldo = randint(1, 10)
    escolhido = randint(1, 10)
    if escolhido == Vinicius:
        print('O escolhido foi o Vinícius!')
        break
    elif escolhido == Melissa:
        print('A escolhida foi a Melissa!')
        break
    elif escolhido == Oswaldo:
        print('O escolhido foi o Oswaldo!')
        break
