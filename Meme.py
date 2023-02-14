def math(var_1, var_2):

    calc = []

    resto = 1

    while resto > 0:
        resto = int(var_1 % var_2)
        var_1 = int(var_1 / var_2)
        calc.append(resto)

    return calc

def invert(var_1):

    result = []
    
    for i in range(len(var_1)):
        result.append(var_1[i][::-1])
    
    return result

def menu():
    menu = input(print(f"1-Tentar novamente.\n2-Sair"))

    if menu == "1":
        main()

    elif menu == "2":
        exit()

    else:
        print(f"Por favor digite uma opção valida.")
        menu()

def main():

    num = input("Digite o numero que deseja converter:")
    base = input("Digite a basa que deseja converter:")

    calc = math(num, base)

    result = invert(calc)

    print(f"O numero {num} em base {base} equivale a: {result}")
    
    menu()


main()