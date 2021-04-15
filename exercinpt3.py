#Peça um número ao usuário e, em seguida, informe se o número é múltiplo de dez ou não.

number_ten = input("Diga um numero para verificarmos se é multiplo de dez: ")
number_ten = int(number_ten)

if number_ten % 10 == 0:
    print("Esse número é multiplo de dez!")
else: 
    print("Esse número nao é multiplo de dez!")    
