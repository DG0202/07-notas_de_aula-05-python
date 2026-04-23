n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

if n1 > n2:
    print(f"O número 1 ({n1}) é maior que o número 2 ({n2})")
elif n2 > n1:
    print(f"O número 2 ({n2}) é maior que o número 1 ({n1})")
else:
    print("Os números são iguais.")