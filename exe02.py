n= int(input('Digite um número inteiro: '))
opcao= int(input('Escolha uma das bases para conversão:\n [1] converter para BINÁRIO\n [2] converter para OCTAL\n [3] converter para HEXADECIMAL\n Qual é a sua opção? '))
binario= bin(n)
octal= oct(n)
hexadecimal= hex(n)

if opcao == 1:
    print(' O número {} digitado é binário {}. '.format(n, binario))
elif opcao == 2:
    print('O número {} digitado é octal {}. '.format(n, octal))
elif opcao == 3:
    print('O número {} é hexadecimal {}'.format(n, hexadecimal))



