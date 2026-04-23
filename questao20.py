nota = -1

while not (0 <= nota <= 10):
    nota = int(input("Insira a sua nota (0 a 10): "))

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")