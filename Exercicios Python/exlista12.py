#Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos
# que possuem altura inferior à média de altura desses alunos
from random import randint, uniform

alunos={}
lista=[]
soma = tot =0
for i in range(0, 30):
    alunos['idade'] = randint(7, 20)
    alunos['altura'] = round(uniform(1, 1.8), 2)
    lista.append(alunos.copy())
    soma += alunos['altura']
media = soma/len(lista)

for a in lista:
    if a['idade'] >=13 and a['altura'] <= media:
        print(a)
        tot +=1


print(f'A média de altura é de {media:.2f}m')
print(f'Temos {tot} alunos com 13 ou mais anos menores que a média')