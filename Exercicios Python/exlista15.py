#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado)
# Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

notas = []

while True:
    nota= int(input('Digite a nota: '))
    if nota == -1:
        print('OK')
        break
    elif nota < -1:
        print('ERRO, Digite uma nota válida de 0 a 10')
    elif nota > 10 :
        print('ERRO digite uma nota de 0 a 10')
    else:
        notas.append(nota)

print(f'Foram informados {len(notas)} valores')
print([notas])
notas.reverse()
for i in notas:
    print(i)
print(f'A soma das notas é {sum(notas)}')
media = sum(notas)/len(notas)
print(f'A media das notas é de {media:.2f}, são elas: ', end='')
m=0
for i in notas:
    if i >= media:
        m =+ 1
        print(i, end=' ')
print()
maior =0
print(f'As notas maiores que 7 são: ', end='')
for i in notas:
    if i >= 7:
        maior += 1
        print(i, end=' ')
print(f'totalizando {maior} notas')
print('FIIIIIIMMMMM')