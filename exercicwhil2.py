#Escreva um laço em que você pergunte a idade aos usuários e, 
# então, informe-lhes o preço do ingresso do cinema.

ingresso = input("Digite qual sua idade: ")

idade = eval(ingresso)

while idade:
    if idade <= 3:
        print('Seu ingresso é grátis')
        break
    if idade <= 12:
        print("Seu ingresso custa $10") 
        break
    else :
        print("Seu ingresso custa $15")
        break