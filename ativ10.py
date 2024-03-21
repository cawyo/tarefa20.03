uni = int(input("1 - PUCPR\n2 - UNICAMP\n/////////\nDigite a instituição de ensino: "))

while uni !=1 and uni !=2:
    uni = int(input("Digite uma instituição válida: "))

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))

med = nota1+nota2/2

if uni == 1:
    if med >= 7:
        print(f"Universidade: PUCPR\nMédia: {med}\nAluno aprovado")
    elif med < 7 and med >= 4:
        print(f"Universidade: PUCPR\nMédia: {med}\nAluno em exame")
    else:
        print(f"Universidade: PUCPR\nMédia: {med}\nAluno reprovado")
else:
    if med >= 5:
        print(f"Universidade: UNICAMP\nMédia: {med}\nAluno aprovado")
    else:
        print(f"Universidade: UNICAMP\nMédia: {med}\nAluno em exame")

        
