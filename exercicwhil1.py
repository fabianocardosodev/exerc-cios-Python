# Escreva um laço que peça ao usuário para fornecer 
# uma série de ingredientes para uma pizza até 
# que o valor 'quit' seja fornecido. 


prompt = "\nDiga os ingredientes desejados em sua pizza: "
prompt += "\nPara finalizar digite 'fim'."

pizza = True
while pizza:
    message = input(prompt)
    if message == 'fim':
        pizza = False
    else: 
        print("Vamos incluir o ingrediente " + message + " em sua pizza!")

