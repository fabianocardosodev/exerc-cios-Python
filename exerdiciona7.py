#cria um dicionario 
#cada chave possui em valores 1 ou mais elementos
#depois imprimi chaves e valores 


numeros_favoritos = {
    'josé' : [30 , 15],
    'mateus' : [17 , 30],
    'adriana': [25, 50 , 100],
}

for name, numeros in numeros_favoritos.items():
    print('\nEsse é ' + name.title() + ' e seus numeros favoritos são: ')
    print(numeros)
