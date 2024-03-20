idade = int(input("Digite sua idade: "))

if idade <16:
    print("Não é eleitor")
elif idade>= 16 and idade<18:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatório")