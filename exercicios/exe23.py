from random import randint
tentativa = 0
jogador = int(input('Digite um número de 0 a 10: '))
comp = randint (0, 10)
while comp != jogador:
    tentativa += 1
    jogador = int(input('Digite um número de 0 a 10: '))
    if jogador < comp:
        print ('Mais... tente novamente!')
    else:
        print ('Menos... tente novamente!')
print (f'Acertou com {tentativa +1} tentativas')  
    
'''# exercicio feito pelo professor 
from random import randint
computador = randint (0, 10)
print ('Acabei de pesnar em um número de 0 a 10 ')
print ('Consegue adivinhar qual número foi?')
acertou = False
palpite= 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
             print ('Mais... tente novamente!')
        elif jogador > computador:
             print ('Menos... tente novamente!')
print (f'Acertou! com {palpite} Tentativas!')'''
