# Você pode armazenar seu prompt em uma variável e passá-la para a função input(). 
# Isso permite criar seu prompt com várias linhas e escrever uma instrução input() clara. 

prompt = "Se você nos disser quem é,podemos personalizar as mensagens que você vê."
prompt += "\nQual é o seu nome?"

name = input(prompt)
print("Olá " + name + "! Seja bem vindo! " )
