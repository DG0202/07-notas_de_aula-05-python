num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2: 
    print(f"{num2} é maior que {num1}")
elif num1 == num2:
    print("Os números são iguais")