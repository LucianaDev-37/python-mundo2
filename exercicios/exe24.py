from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0 # Usaremos essa variável para controlar o loop

while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    
    opcao = int(input('>>>> Qual é a sua opção? '))

    # Tudo isso agora está DENTRO do while (identado para a direita)
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    
    elif opcao == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} é {mult}')
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior número é {maior}')
    
    elif opcao == 4:  
        print('Informe os números novamente:') 
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    
    elif opcao == 5:
        print('Finalizando...')
    
    else:
        print('Opção inválida. Tente novamente.')
    
    print('=-=' * 10)
sleep (2)
print('Fim do programa! Volte sempre.')