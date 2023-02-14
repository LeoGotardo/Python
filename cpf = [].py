cpf = []
nome = ()
lista = {}

def main2():
    menu = input(f"qual opção você deseja acessar? \n 1-Adicionar novo CPF. \n 2-Verificar CPF. \n")
    main(menu)

def main(pri):
  if pri == "1":
    lista = {
  input(f"nome:"): input(f"cpf:"),
    }
    main2()

  elif pri == "2":
    print(dict(lista))

  else:
    print("Numero invalido")
    main2()

main2()