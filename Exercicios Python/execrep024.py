#Faça um programa que calcule o mostre a média aritmética de N notas.
soma = c = 0
continua = ' '

while True:
    nota = float(input('Digite uma nota: '))
    if nota > 10 or nota < 0:
        print('Nota inválida, digite um valor entre 0 e 10')
    c+=1
    soma += nota
    continua = str(input('Deseja adicionar mais alguma nota? [S/N]')).upper().strip()
    if continua == 'N':
        break

print(f'Foram digitadas {c} notas e a média total foi de {soma/c}')
