favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'c', 
    'edward' : 'ruby',
    'phil' : 'pyhton'
}

# O METODO KEYS UTIL QUANDO NAO NECESSITAMOS TRABALHAR 
# COM TODOS OS VALORES,POREM VOCE PODE EXPLICITA-LO OU NAO
# POIS O CODIGO TRABALHARA DA MESMA FORMA

for name in favorite_languages.keys():
    print(name.title())
