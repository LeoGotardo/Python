def main():

    num = int(input(f"Enter the number you want to convert:"))
    base = int(input(f"Enter the base you want to convert from:"))

    convert(num,base)
    main()

def convert(pri,sec):

    number_list = []
    number_anser = []

    while pri <= sec:
        prov = pri % sec
        pri = round(pri / sec)

        number_list.append(prov)   

        for i in range(len(number_list)):
            number_anser.append(number_list[i][::-1])

    print(f"A lista é: {number_list}")

main()
    
