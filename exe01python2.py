casa= str(input('Qual o valor da casa que você quer comprar? R$' ))
salario= str(input('Qual o seu salário mensal? R$'))
anos= int(input('Em quantos anos você quer pagar a casa? '))


casa = casa.replace('.', '')      # remove separador de milhar
casa = casa.replace(',', '.')     # troca vírgula por ponto
casa = float(casa)                # converte para número
salario = salario.replace('.', '')
salario = salario.replace(',', '.')
salario = float(salario)

meses= anos * 12
prestacao_mensal= casa/meses
minimo= (salario * 30) / 100
if prestacao_mensal <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação mensal será de R$ {:.2f}'.format(prestacao_mensal))

