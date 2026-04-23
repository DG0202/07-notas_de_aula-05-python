n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 4: "))

med = (n1 + n2 + n3)/3
print(med)
if med >= 5 and med < 7:
    print("Você está de recuperação")
elif med > 7:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado")