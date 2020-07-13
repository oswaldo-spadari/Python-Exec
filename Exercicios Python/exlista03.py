#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
nota = []
for i in range(1, 5):
    nota.append(float(input(f'Digite a {i} nota: ')))

media = sum(nota) / len(nota)
print(f'A média das notas {nota} é {media}')
