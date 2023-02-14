cartao = int(input('Digite a quantidade total de cartões : '))
cartao_main = cartao - 2
taxa = 0

for x in range(2): 
    print('Cartão ' + str(x+1) + 'º  : 0' )

for i in range(cartao_main):
    taxa += 500   
    print('Cartão ' + str(i+3) + 'º  :' ,taxa)

Soma = (500 + taxa ) * cartao_main / 2 
   
print('Total R$ : ',Soma)
