pessoas_jantar = input("Boa noite,quantas pessoas estão para jantar?:")
pessoas_jantar = int(pessoas_jantar)

if pessoas_jantar >= 8:
    print("Desculpe como vocês estão em " + str(pessoas_jantar)
    + " pessoas,precisarão aguardar termos mesas disponiveis.")
else:
    print("Ok! Por favor me acompanhe até sua mesa!")
