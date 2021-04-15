#devemos usar a funcao int() para converter a informação do input 
#em numero inteiro

height = input("Qual sua altura em centimetros?: ")
height = int(height)

if height <= 120:
    print("Você não pode ir na montanha russa!")
else:
    print("Pode subir no carrinho!")    


