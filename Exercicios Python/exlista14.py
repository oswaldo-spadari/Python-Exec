#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


tel = str(input('Telefonou para a vítima?'))
local = str(input('Esteve no local do crime?'))
perto = str(input('Mora perto da vítima?'))
deve = str(input('Devia para a vítima?'))
work = str(input('Já trabalhou com a vítima?'))
lista=[tel, local, perto, deve, work]
s = 0
print(lista)
for i in lista:
    if i == 's':
        s += 1

print(s)
if s == 5:
    print('Culpado')
elif s == 3 or s == 4:
    print('Cúmplice')
elif s == 2:
    print('Suspeita')
else:
    print('INOCENTE')