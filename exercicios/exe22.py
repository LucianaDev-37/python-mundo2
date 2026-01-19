'''sexo = str(input('Digite "M" sexo masculino e "F" para sexo feminino: ')).upper().strip()[0]#fatiamento pega só a primeira letra m ou f , mesmo digitndo a pavra feminino ou masculino
while sexo != 'M' and sexo != 'F':
    print('Valor inválido, Digite novamente')
    sexo = str(input('Digite "M" sexo masculino e "F" para sexo feminino: ')).upper()
print('Sexo registrado com sucesso!')'''
#resolução do professor
sexo = str(input('informe o sexo M/F: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo registrado com sucesso!')
    
