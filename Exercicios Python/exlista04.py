# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
consoante = 0
for i in range(0, 10):
    letras.append(str(input('Digite a letra: ')))
    if letras[i].upper() not in 'AEIOU':
        consoante += 1
print(f'no total foram {consoante} consoantes. São elas: ', end='')
c = 0
for l in letras:
    if letras[c].upper() not in 'AEIOU':
        print(l, end=' ')
    c += 1
