#dicionarios dentro de dicionario
#muitos usuarios

usuarios = {
    'aeinsten' : {
        'primeiro' : 'albert',
        'segundo' : 'einsten',
        'localização' : 'princeton',
    },

    'mcurie' : {
        'primeiro' : 'marie',
        'segundo' : 'curie',
        'localização' : 'paris',
    },
}

for nome_usuario, info_usuario in usuarios.items():
    print('\nNome_usuario: ' + nome_usuario )
    full_name = info_usuario['primeiro'] + " " + info_usuario['segundo']
    location = info_usuario['localização']

    print('\nNome: ' + full_name.title())    
    print('\nLocalizacao: ' + location.title())