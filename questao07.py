username = str(input("Insira seu nome de usuário: "))
usernameleng = len(username.replace(" ",""))

if usernameleng > 10:
    print(f"Nome de usuário muito longo, {usernameleng} caracteres.")
else:
    print("Nome aceito")