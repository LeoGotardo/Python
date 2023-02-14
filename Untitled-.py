num = (int(input("Digite um número inteiro: ")))
cont = 0
i = 0

while i <= num or cont < 2:
    i = i + 1
    x = num % i
    
if x == 0:
    cont = cont + 1

if cont <= 2:
    print("primo")
else:
    print("não primo")