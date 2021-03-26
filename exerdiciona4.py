# cria dicionarios com informações pessoas
pessoa_1 = {'nome':'carla','sobrenome':'silva','idade':18,'cidade':'ribeirao'}
pessoa_2 = {'nome':'eduardo','sobrenome':'nogueira','idade':20,'cidade':'olimpia'}
pessoa_3 = {'nome':'carla','sobrenome':'silva','idade':18,'cidade':'barretos'}

#inclui esses dicionarios em uma lista
pessoas = [ pessoa_1,pessoa_2,pessoa_3]

#percorre essa lista com laço for para apresentar infos
for pessoa in pessoas:
    print('\nDados: ' , pessoa)

