#cria uma lista vazia para armazenar
aliens = []

#cria 30 aliens e inclui na lista
for alien_number in range(30):
    new_alien = { 'colors' : 'green' , 'points' : 15}
    aliens.append(new_alien)

#mostra 5 alienigenas primeiros
for alien in aliens[:5]:
    print(alien)
print("...")

# Mostra quantos alienígenas foram criados 
print( "Numero total de aliens criados: " + str(len(aliens)))
