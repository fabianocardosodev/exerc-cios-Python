favorite_languages = {
    'carlos': ['python', 'ruby'],
    'lucas' : [ 'c'],
    'antony': ['java','go'],
    'eduardo':['python','c++']
}
# aninhar uma lista em um dicionário
# sempre que quiser que mais de um valor 
# seja associado a uma única chave em um dicionário.

for name, languages in favorite_languages.items():
    if (len(languages)) == 1:
        print( name.title() + ' , sua linguagem favorita é: '  ) 
        print(languages)
        
    else:   
        print('\n' +  name.title() + ' ,suas linguagens favoritas são: ' )
        print(languages)

