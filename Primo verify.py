cont = 2
num = int(input(f"Digite os numero a verificar:\n"))
num2 = int(input(f"Digite os numero a verficar:\n"))
num3 = int(input(f"Digite os numero a verificar:\n"))

def verify(pri):
  if pri == 0:
    print("divisao por 0 impossivel.")
    return

  while cont < pri and cont > 1:
    test = test + pri % cont
    cont =+ 1
  
  if test < 0:
    return False #nao e primo
  else:
    return True #e primo
if verify(num) == True or verify(num2) == True or verify(num3) == True :
  print("Tem algum primo.")

else:
  print("Não tem primo.")
