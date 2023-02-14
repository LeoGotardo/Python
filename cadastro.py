id = []
num_de_cadastro = len(id)

def cadastro():
    nome = (input(f"Digite o nome:"))
    idade = (input(f"Digite a idade de {nome} :"))
    cadastro = [nome,idade]
    id.append(cadastro)
    print(num_de_cadastro)

def procurar():
    num_id = input(f"digite o numro de cadastro:")
    

resposta = input(f"Oque quer fazer? \n 1-Cadastro \n 2-Procura \n")


if resposta == 1 :
    cadastro()
elif resposta  == 2 :
    procurar()