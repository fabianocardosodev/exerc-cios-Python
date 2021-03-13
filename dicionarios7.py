favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'c', 
    'edward' : 'ruby',
    'phil' : 'Python'
}

print('As seguintes linguagens foram mencionadas: ')
# usamos o metodo values para apresentar os valores no dicionario sem as chaves
# A instrução for, nesse caso, extrai cada valor do dicionário e o armazena na variável language.
# Quando esses valores são exibidos, temos uma lista de todas as linguagens escolhidas
for language in favorite_languages.values():
    print(language.title())
    