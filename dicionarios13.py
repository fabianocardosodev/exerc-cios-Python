#armazena informcoes sobre uma pizza que esta sendo pedida
pizza = {
    'massa' : 'grossa',
    'coberturas' : ['mussarela' , 'calabresa'],
}

#resume pedido
print('Voce pediu : ' + pizza['massa'] + "-massa pizza "
        + 'com as seguintes coberturas:')

#usamos laço for para exibir as coberturas pedidas
for cobertura in pizza['coberturas']:
    print('\t' + cobertura)

