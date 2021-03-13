favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'c', 
    'edward' : 'ruby',
    'phil' : 'Python'
}

# funcao sorted para apresentar uma copia ordenada das chaves
for name in sorted(favorite_languages.keys()):
    print(name.title() + ' ,obrigado por participar de nossa enquete!' )

