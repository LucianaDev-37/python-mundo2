soma = 0 #acumulador
contador = 0 #conta quantos números foram digitados
maior= 0
menor = 0
resposta = 'S' #decide se o while continua
while resposta == 'S':
    n= int(input('Digite um número: '))
    
    soma = soma + n
    contador = contador + 1

    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]

if contador > 0:
    media = soma / contador
    print(f'Você digitou {contador} números e a média foi {media:.2f}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print('Nenhum número foi digitado.')

print('Fim')
