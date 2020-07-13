# Faça um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos
# concorrentes # e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
#
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

urna = {}
votos = []
w = u = l = n = m = o = 0
while True:
    try:
        print('-' * 50)
        print(f'{"SISTEMA DE VOTO":^50}')
        print('-' * 50)
        vot = int(input('Qual o melhor Sistema Operacional para uso em servidores?\n'
                         '1- Windows Server\n'
                         '2- Unix\n'
                         '3- Linux\n'
                         '4- Netware\n'
                         '5- Mac OS\n'
                         '6- Outro\n'
                         '--------------------------------------------------\n'
                         'Digite sua opção: '))

    except ValueError:
        print('\033[31mValor inválido!!Digite apenas valores conforme o menu!\033[m')
    else:
        if vot == 0:
            print('-'*50)
            print('Obrigado e até logo!!!!')
            break
        elif vot > 6 or vot < 0:
            print('\033[31mValor inválido!!Digite apenas valores conforme o menu!\033[m')
        else:
            if vot == 1:
                w += 1
                urna['Windows Server'] = w
            elif vot == 2:
                u += 1
                urna['Unix'] = u
            elif vot == 3:
                l += 1
                urna['Linux'] = l
            elif vot == 4:
                n += 1
                urna['Netware'] = n
            elif vot == 5:
                m += 1
                urna['Mac OS'] = m
            else:
                o += 1
                urna['Outros'] = o
            votos.append(vot)
div = len(votos)/100
print('-'*50)
print(f'{"SISTEMA OPERACIONAL":<30}{"VOTOS":^10}{"%":>10}')
print(f'{"-"*19:<30}{"-"*5:^10}{"-"*3:>10}')
for k,v in urna.items():
    print(f'{k:<30} {v:^10}{v/div:>10.2f}%')
print(f'{"-"*19:<30}{"-"*5:^10}{"-"*3:>10}')
print(f'{"Total":<30}{len(votos):^10}')
