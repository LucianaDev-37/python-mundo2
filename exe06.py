from datetime import date
nascimento = int(input('Digite o ano de seu nascimento? '))
ano = date.today().year
idade = ano - nascimento
print('Sua idade é de:{} '.format(idade))
if idade <= 9:
    print('MIRIM! ')
elif idade <= 14:
    print('INFANTIL! ')
elif idade <= 19:
    print('JÚNIOR! ')
elif idade <= 20:
    print('SÊNIOR! ')
else:
    print('MASTER! ')





