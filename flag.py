# Para um programa que deva executar somente enquanto muitas condições forem verdadeiras,
# podemos definir uma variável que determina se o programa como um todo deve estar ativo.
# Essa variável, chamada de "flag", atua como um sinal para o programa. 

prompt = "\nDiga-me alguma coisa e eu repetirei para você!"
prompt += "\nEnter 'sair' para o fim do programa "

active = True
while active:
    message=input(prompt)
    if message == "sair":
        active = False
    else:
        print(message)