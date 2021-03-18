favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'c', 
    'edward' : 'ruby',
    'phil' : 'Python'
}

print('As seguintes linguagens foram mencionadas: ')
for language in set(favorite_languages.values()):
    print(language.title())
    