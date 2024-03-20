a = float(input("Informe a variável A:\n"))
b = float(input("Informe a variável B:\n"))
c = float(input("Informe a variável C:\n"))

delta= b**2 - (4*a*c)

if delta > 0:
    print("Existem duas raizes reais distintas")
elif delta == 0:
    print("Existem duas raizes reais iguais")
else:
    print("Existem duas raizes imaginárias conjugadas")