cpf = []
soma1 = 0
soma2 = 0

# o for vai pegar todos os dígitos cpf e colocar em uma lista
for i in range(1, 12 ,1):
    digito = int(input(f'Informe o {i} digito do seu CPF: '))
    cpf.append(digito)
# imprimi

# o for vai multiplicar cada digito da sua posicao comecando em 1,
# até chegar nos digitos verificadores,os quais nao entram na conta
# Depois vai apresentar soma das multiplicações
for i in range(1, 10, 1):
    soma_dig1 = cpf[i - 1] * 1
    soma1 += soma_dig1
# print(soma1) 

resto1 = (soma1 % 11)
#print(verif_dig1)
verif_dig1 = int(resto1 / 100)
# print(unidade)

# o for vai multiplicar cada digito da sua posicao comecando em 1,
# até chegar nos digitos verificadores,os quais nao entram na conta
# Depois vai apresentar soma das multiplicações
for i in range(0, 9, 1):
    soma_dig2 = cpf[i] * i
    soma2 += soma_dig2

verif_dig2 = int(soma2 % 11)



if verif_dig1 == cpf[9] and verif_dig2 == cpf[10]:
    print('CPF válido!')
else:
    print('CPF inválido!')    

