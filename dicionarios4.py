favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'c', 
    'edward' : 'ruby',
    'phil' : 'Python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print('Olá ' + name.title() + 
               ' vejo que seu idioma favorito é ' + 
               favorite_languages[name].title() + '!')
