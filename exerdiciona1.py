programação = {
    'while' : 'enquanto',
    'else' : 'senão',
    'if' : 'se',
    'iteração' : 'repetição',
    'identação' : 'tabulação código'
}

programação['widgets'] = 'ferramentas'
programação['device'] = 'aparelho'
programação['commit'] = 'alteração'

print ('Palavras e significados na programação: ' )

for key,value in programação.items():
    print("\nKey: " + key )
    print("Value: " + value)


