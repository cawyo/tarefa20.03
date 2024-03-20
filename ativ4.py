nota = float(input("Digite a nota do aluno:\n"))
if nota >= 7:
    print("ALUNO APROVADO")
elif nota < 7 and nota >= 4:
    print("ALUNO EM RECUPERAÇÃO")
else:
    print("ALUNO REPROVADOS")