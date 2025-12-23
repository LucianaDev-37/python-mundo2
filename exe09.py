jogador= str(input('Digite 1 = papel, 2 = tesoura, 3 = pedra: ')).strip().lower()

if jogador == '1' or jogador == 'papel':
    print('PAPEL! ')

elif jogador == '2' or jogador == 'tesoura':
    print('TESOURA! ')

elif jogador == '3' or jogador == 'pedra':
    print('PEDRA! ')
    exit()

else:
    print('Opção inválida.')

import random 
opcao = ['papel','tesoura','pedra']
random.choice(opcao)

# Computador
opcoes = ['papel', 'tesoura', 'pedra']
computador_escolha = random.choice(opcoes)

print(f'Você escolheu: {jogador}')
print(f'O computador escolheu: {computador_escolha}')

# Resultado
if jogador == computador_escolha:
    print('Empate!')
elif (
    (jogador == 'papel' and computador_escolha == 'pedra') or
    (jogador == 'tesoura' and computador_escolha == 'papel') or
    (jogador == 'pedra' and computador_escolha == 'tesoura')
):
    print('Você ganhou!')
else:
    print('O computador ganhou!')

