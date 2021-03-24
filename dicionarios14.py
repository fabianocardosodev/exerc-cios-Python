favorite_language = {
    'carlos': ['python', 'ruby'],
    'lucas' : [ 'c'],
    'antony': ['java','go'],
    'eduardo':['python','c++']
}
# aninhar uma lista em um dicionário
# sempre que quiser que mais de um valor 
# seja associado a uma única chave em um dicionário.

for name, languages in favorite_language.items():
    print('\n' +  name.title() + ' ,sua linguagens favoritas são: ' )
    for language in languages():
        print('\t' + language.title())
