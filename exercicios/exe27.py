i1 = 0
i2 = 1
n = int(input('Quantos termos você quer ver? '))

print(f'{i1} - {i2}', end=' - ')

i = 3 
while i <= n:
    i3 = i1 + i2
    
    print(f'{i3}', end=' - ')
    
    i1 = i2
    i2 = i3
    
    i = i + 1

print('FIM')