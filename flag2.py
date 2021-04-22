# Para um programa que deva executar somente enquanto muitas condições forem verdadeiras,
# podemos definir uma variável que determina se o programa como um todo deve estar ativo.
# Essa variável, chamada de "flag", atua como um sinal para o programa. 

prompt = '\nDiga-me qual filme você gosta: '
prompt += '\n ou Enter com "fim" para encerrarmos conversa'

filme = True
while filme:
    message = input(prompt)
    if message == 'fim':
        filme = False
    else:
        print('Eu tambem gosto de ', message)

