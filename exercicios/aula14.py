'''n = 1
while n != 0:
    n= int(input('Digite um número '))
    print('Fim')'''


'''for c in range(1, 11):
     print(c)
print ('fim')'''

'''i = 1 # começa com 1 pq é o inicio do range
while i < 11: # enquanto o i=1 não chegar a 10
    print(i)
    i += 1 # quando ele volta ao loop soma 1 por ser tmb representado i= i + 1
print ('fim')'''


'''r = 'S'
while r == 'S':
    n = int(input('digite um valor '))
    r = str(input('Quer continuar? [S/N]')).upper ()
print ('fim')'''


par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
       if n % 2 == 0:
        par += 1
       else:
        impar += 1

print(f'Voçê digitou {par} número pares e {impar} números imapares')


