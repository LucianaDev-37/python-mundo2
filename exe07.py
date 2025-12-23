peso= float(input('Digite o seu peso (ex.:69.2): '))
altura= float(input('Digite a sua altura (ex.:1.70): '))
imc= peso / (altura * altura)
print('IMC de: {:.2f} '.format(imc))

if imc < 18.5:
    print('Abaixo do peso. ')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal. ')
elif imc >= 25 and imc < 30:
    print('Sobrepeso. ')
elif imc >= 30 and imc < 40:
    print('Obesidade. ')
else:
    print('Obesidade mórbida. ')


