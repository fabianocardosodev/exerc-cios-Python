rios = {
    'nilo' : 'egito',
    'rio grande' : 'brasil',
    'rio parana' : 'brasil'
}

for key,value in rios.items():
    print(' O rio ' + key.title() + ' corre pelo ' + value.title())

for key in rios.keys():
    print(key.title())

for value in rios.values():
    print(value.title())
