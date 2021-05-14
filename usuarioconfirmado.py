#Começa com os usuarios que precisam ser verificados,
# e com uma lista vazia para armazenar os usuarios confirmados
unconfirmed_users = ["alice","brian","candace"]
confirmed_users = []

#verifica cada usuario até que não haja mais usuarios não confirmados
#transfere cada usuario verificado para a lista de usuarios conf
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verificar usuario: " + current_user.title())
    confirmed_users.append(current_user)

# Exibe todos os usuarios confirmados
print("\nOs seguintes usuarios tem estado confirmado: ")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())    