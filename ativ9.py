idade=int(input("Digite a idade: "))
anos=int(input("Digite os anos de serviço: "))

if idade >= 60 and anos >= 25 or idade>=65 or anos>=30:
    print("Elegivel a aposentadoria")
else:
    print("Não elegivel a aposentadoria")