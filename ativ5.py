altura = float(input("Digite a altura(em metros): "))
sexo = input("Digite o sexo(M ou F): ")

while sexo !="M" and  sexo != "F":
    sexo = str(input("Digite apenas M ou F: "))

pesoIdeal = 0

if sexo == 'M':
    pesoIdeal=(72.7*altura)-58
else:
    pesoIdeal=(62.1*altura)-44.7

print(f"O peso ideal é: {pesoIdeal}")