#Definiremos um valor de saída e então deixaremos o programa executando 
# enquanto o usuário não tiver fornecido o valor de saída "fim"

prompt = "\nDiga-me alguma coisa e eu repetirei para você!"
prompt += "\nEnter para o fim do programa "

message = " "
while message != "fim":
    message=input(prompt)
    print(message)