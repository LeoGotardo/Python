def calc(pri):
   n = 0
   result = 0
   
   while n <= len(pri):
      result = int(pri[n]) * int(pri[n+1]) + result
      n = n+2
      print(result)

      return result


def main():
   num = input(f"Digite os numeros da multipliacao:\n")
   lista = num.split(",")

   result = calc(lista)

main()