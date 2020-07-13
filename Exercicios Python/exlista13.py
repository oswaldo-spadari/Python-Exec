# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

ano = [['Janeiro', 21.5], ['Fevereiro', 24.4], ['Março', 20.5], ['Abril', 18.5], ['Maio', 16.6], ['Junho', 15.5],
       ['Julho', 15.4], ['Agosto', 16.2], ['Setembro', 17.4], ['Outubro', 18.5], ['Novembro', 19.8], ['Dezembro', 20.3]]

soma = media = 0
tem = 1
for i in ano:
    soma += i[1]
    media = soma/12

print(f'A temperatura média em SP é de {media:.2f}°C')
print(f'Os meses com temp. acima da média foram: ', end='')
for i in ano:
    if i[1] >= media:
        print(i[0], end=' ')
