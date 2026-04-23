payment = float(input("Insira o seu salário: "))

if payment > 3000:
    tax = payment * 0.15
    allpayment = payment - tax
else:
    tax = payment * 0.075
    allpayment = payment - tax
print(f"O seu salário, após impostos, será de {allpayment}")