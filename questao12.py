word = str(input("Insira uma palavra: "))

word.lower().startswith('a')
if word.startswith("A") or word.startswith("a"):
    print("A palavra começa com A")
else:
    print("A palavra não começa com A")