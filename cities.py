# A instrução break direciona o fluxo de seu programa; 
# podemos usá-la para controlar quais linhas de código são ou não são executadas,
# de modo que o programa execute apenas o código que você quiser, quando você quiser

prompt = "\nPor favor coloque o nome da cidade que você já visitou: "
prompt += "\n Para sair dessa conversa digite 'sair'."

while True:   
    city = input(prompt)
    if city == 'sair':
        break
    else:
        print("Eu amo viajar para: " + city.title())
