#cria uma lista vazia para armazenar
aliens = []

#cria 30 aliens e inclui na lista
for alien_number in range(0,30):
    new_alien = { 'colors' : 'green' , 'points' : 5, 'speed': 'slow'}
    aliens.append(new_alien)

#altera 3 primeiros aliens
for alien in aliens[0:3]:
    if alien ['colors'] == 'green':
        alien['colors'] = 'blue'
        alien['points'] = 10
        alien['speed'] = 'medium'

#mostra os 5 primeiros aliens
for alien in aliens[0:5]:
    print(alien)
print("...")

# Mostra quantos alienígenas foram criados 
print( "Numero total de aliens criados: " + str(len(aliens)))
