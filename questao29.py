peso = float (input("Digite seu peso:"))
altura = float (input("Digite sua altura:"))
IMC = peso/altura**2
if IMC <= 25:
    print("Peso normal")
else:
    print("Acima do peso")