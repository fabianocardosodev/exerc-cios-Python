favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'c', 
    'edward' : 'ruby',
    'phil' : 'pyhton'
}

favorite_languages['carlos'] = 'ruby'
favorite_languages['eduarda'] = 'java'
favorite_languages['silas'] = 'php'
favorite_languages['mateus'] = 'javascript'


friends = ['carlos','silas','flavio','lucas','eduarda']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print('Olá ' + name.title() + 
        ' que bom que participaram de nossa enquete!')

if 'flavio' not in favorite_languages.keys():
    print( 'Olá Flavio!Não participou de nossa enquete? Participe!')
            
