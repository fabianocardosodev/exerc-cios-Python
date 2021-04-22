#considere um laço que conte de 1 a 10, 
# mas apresente apenas os números ímpares desse intervalo

numero_atual = 0
while numero_atual < 10:
    numero_atual += 1
    if numero_atual % 2 == 0:
        continue

    print(numero_atual)