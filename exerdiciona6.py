#cria um dicionario 
#cada chave possui em valores 1 ou mais elementos
#depois imprimi chaves e valores 


lugares_favoritos = {
    'alan' : ['copacabana','fernando noronha'],
    'lucas' : ['rio grande do norte'],
    'monica': ['rio de janeiro','porto seguro','ilha bela'],
}

for name, lugares in lugares_favoritos.items():
    print('\n' + name.title() + ' seus lugares favoritos são: ')
    print(lugares)
