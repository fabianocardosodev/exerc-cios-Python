#Escreva um laço em que você pergunte a idade aos usuários e, 
# então, informe-lhes o preço do ingresso do cinema.
#outra forma

prompt = "\nPara informar o valor do ingresso diga qual sua idade: "
prompt += "\nou Entre com '0'(zero) para encerrar consulta: "

ingresso = True
while ingresso:
    message = eval(input(prompt))
    if message == 0:
        break    
    if message <= 3:
        print("Seu ingresso é grátis")
        break
    if message <= 12:
        print("O ingresso custa $10")
        break
    else:
        print('seu ingresso custa $15')
        break
    