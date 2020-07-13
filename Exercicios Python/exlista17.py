def pos(num):
    if num == 1:
        return 'Primeiro'
    elif num == 2:
        return 'Segundo'
    elif num == 3:
        return 'Terceiro'
    elif num == 4:
        return 'Quarto'
    elif num == 5:
        return 'Quinto'
    else:
        return 'Nao é contabilizado depois do quinto'


#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
# atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.
todos = []
atletas={}
notas = []
while True:
    notas.clear()
    print(''*30)
    nome = str(input(('Nome do atleta: '))).strip().title()
    if nome == '':
        break
    else:
        for i in range(1, 6):
            notas.append(float(input(f'Nota do {pos(i)} Salto: ')))
    atletas['atleta'] = nome
    atletas['notas'] = notas.copy()
    atletas['media'] = sum(notas)/len(notas)
    todos.append(atletas.copy())

print('='*30)
print('Resultado Final: ')
for i in todos:
    for k, v in i.items():
        print(f'{k}: {v}')

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9m
