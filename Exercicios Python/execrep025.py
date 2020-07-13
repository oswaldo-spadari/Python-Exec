#Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,
# 26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = c = 0

while True:
    idade = int(input('Qual a idade da pessoa: '))
    soma += idade
    c += 1
    cont = str(input('Deseja adicionar mais alguma idade? [S/N]')).upper().strip()
    if cont == "N":
        break
media = soma / c
if media < 26:
    print('A média da turma é jovem')
elif media < 61:
    print ('A média da turma é adulta')
else:
    print ('A media da turma é idosa')
