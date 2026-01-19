'''soma = 0
c = 0
n = int(input('Digite um número [999 para parar]: '))
while c != 999:
    if n == 999:
       break
    else:
        soma = soma + n
        c = c + 1
    n = int(input('Digite outro: ')) 
print(f'Você digitou {c} números e a soma entre eles foi {soma}.')
print('Fim')'''
 
         
soma = 0
c = 0
parar = False
while not parar:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
       parar = True 
    else:
        soma = soma + n
        c = c + 1
    
print(f'Você digitou {c} números e a soma entre eles foi {soma}.')
print('Fim')
 
         
