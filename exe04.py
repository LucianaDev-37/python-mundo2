
from datetime import date
nascimento= int(input('Digite o ano do seu nascimento: '))
ano= date.today().year
idade= ano - nascimento
tempo_falta= 18 - idade
tempo_passou= idade - 18
if idade < 18:
    print ('Ainda não é hora de se alistar, faltam {} anos para completar 18anos. '.format (tempo_falta))
elif idade == 18:
    print ('Ja é exatamente a hora de se alistar ')
elif idade > 18:
    print ('Já passou do tempo do alistamento, passaram {} anos dos 18 anos. '.format(tempo_passou))


