#remove as instancias de valor especifico de uma lista
#funçao "remove"

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
