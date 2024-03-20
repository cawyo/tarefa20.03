uni = int(input("1 - PUCPR\n2 - UNICAMP\n/////////\nDigite a instituição de ensino: "))

x = float(input("Digite a nota do primeiro bimestre: "))
y = float(input("Digite a nota do segundo bimestre: "))

med = x+y/2

if uni == 1:
    if med >= 7:
        print(f"Universidade: PUCPR\nMédia: {med}\nAluno aprovado")
    elif med < 7 and med >= 4:
        print(f"Universidade: PUCPR\nMédia: {med}\nAluno em exame")
    else:
        print(f"Universidade: PUCPR\nMédia: {med}\nAluno reprovado")
if uni == 2:
    if med >= 5:
        print(f"Universidade: UNICAMP\nMédia: {med}\nAluno aprovado")
    else:
        print(f"Universidade: UNICAMP\nMédia: {med}\nAluno exame")
        
