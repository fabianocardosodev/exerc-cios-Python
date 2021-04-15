number = input("Digite um numero e te direi se é par ou impar: ")
number = int(number)
#Com a entrada sendo ref numericamente a usamos para operações matematicas, 
# operador modulo para saber o resto. 
if number % 2 == 0:
    print("Esse numero é par.")
else:
    print("Esse numero é impar.")