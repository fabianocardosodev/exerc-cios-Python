# Crie um dicionário com informações sobre cada cidade 
# e inclua o país em que a cidade está localizada,
# a população aproximada e um fato sobre essa cidade

cidades = {
    'ribeirao_preto' : {
        'pais' : 'brasil',
        'populacao' : '800mil',
        'fato_historico' : 'grande produtor café',
       },   
    
    'batatais' : {
        'pais' : 'brasil',
        'populacao' : '90mil',
        'fato_historico' : 'produtor leite'
       }, 

    'olímpia' : {
        'pais' : 'brasil',
        'populacao' :'60mil',
        'fato_historico' : 'aguas termais',
     }, 

}

# o laço percorre as informações em cada dicionario
# criamos variaveis que sao atribuidas dos valores especificos para melhor vizualização
for nome_cidade, info_cidade in cidades.items():
    print( '\nCidade: ' + nome_cidade)
    pais = info_cidade['pais']
    pop =  info_cidade['populacao'] 
    fact =  info_cidade['fato_historico']

    print('\tPaís: ' + pais)
    print('\tPopulação: ' + pop)
    print('\tCuriosidade: ' + fact)
