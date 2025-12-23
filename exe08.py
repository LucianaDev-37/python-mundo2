preco_produto = float(input('Digite o valor do produto:R$ '))
forma_pagamento = int(input('''Digite a forma de pagamento ex.: debito/pix = 1, cartão à vista = 2, cartão parcelado = 3: '''))

debito_pix = 1
cartao_a_vista = 2
cartao_parcelado = 3

# debito ou pix
if forma_pagamento == 1:
    desconto = preco_produto * 0.10
    valor_final = preco_produto - desconto
    print('Forma de pagamento selecionada com sucesso! Valor final com desconto: R$ {:.2f}'.format(valor_final))


# cartão a vista
elif forma_pagamento == 2:
    desconto = preco_produto * 0.05
    valor_final = preco_produto - desconto
    print(''' Forma de pagamento selecionada com sucesso! Valor final com desconto: R$ {:.2f}'''.format(valor_final))
# quantas parcelas selecionadas 
elif forma_pagamento == 3:
    parcelas = int(input('Em quantas parcelas deseja pagar?.(ex:.2,3,10) '))

    # 1x no cartão (5% desconto)
    if parcelas == 1:
        desconto = preco_produto * 0.05
        valor_final = preco_produto - desconto
        print('Cartão parcelado em 1x (5% de desconto)')
        print(f'Valor final a pagar: R$ {valor_final:.2f}')

    # 2x no cartão (preço normal)
    elif parcelas == 2:
        valor_final = preco_produto
        valor_parcela = valor_final / parcelas
        print('Cartão parcelado em 2x (sem juros)')
        print(f'Valor total: R$ {valor_final:.2f}')
        print(f'Valor de cada parcela: R$ {valor_parcela:.2f}')

    # 3x ou mais (20% de juros)
    elif parcelas >= 3:
        juros = preco_produto * 0.20
        valor_final = preco_produto + juros
        valor_parcela = valor_final / parcelas
        print(f'Cartão parcelado em {parcelas}x (20% de juros)')
        print(f'Valor total: R$ {valor_final:.2f}')
        print(f'Valor de cada parcela: R$ {valor_parcela:.2f}')

    else:
        print('Número de parcelas inválido.')

else:
    print('Forma de pagamento inválida.')




