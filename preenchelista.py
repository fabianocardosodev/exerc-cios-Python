#pede a quantidade de entrada necessaria a cada passagem 
#pelo laço while

respostas = {}

#DEFINE uma flag para indicar que a enquete está ativa
polling_active = True

while polling_active:
    #pede o nome da pessoa e a resposta
    name = input("\nQual o seu nome?")
    resposta = input("Qual montanha você gostaria de escalar?")
    #armazena a resposta no dicionario
    respostas[name] = resposta
    #descobre se outra pessoavai responder a enquete
    repete = input ("voce gostaria de outra pessoa pra responder a enquete ? (yes/no)")
    if repete =='no':
        enquete_active = False

#a enquete foi concluída,mostra os resultados
    print("\n----Enquete Resultados----")
    for name,resposta in respostas.items():
        print(name + " Gostaria de escalar: " + resposta + " . ")
