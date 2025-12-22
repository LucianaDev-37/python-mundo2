nota1= float(input('Digite a sua primeira nota: '))
nota2= float(input(' Digite a sua segunda nota: '))
media= (nota1 + nota2) / 2
print('Sua média é {}'.format(media))

if media < 5.0:
    print('Reprovado! ')
elif media >= 5.0 and media < 7.0 :
    print('Recuperação! ')
elif media >= 7.0:
    print('Aprovado! ')
