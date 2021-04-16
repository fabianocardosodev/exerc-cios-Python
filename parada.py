#Um laço que comece com while True u executará indefinidamente, 
# a menos que alcance uma instrução break. 

prompt = "\nDiga a cidade que você visitou: "
prompt += "\n(Digite 'sair' quando terminar)"

while True:
    city = input(prompt)

    if city == 'sair':
        break

    else:
        print("Eu adoraria ir para " + city.title())

