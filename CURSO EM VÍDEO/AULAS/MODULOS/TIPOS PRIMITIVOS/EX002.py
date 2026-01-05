n1 = input("DIGITE UM VALOR: ")
n2 = int(input("DIGITE OUTRO VALOR: "))
n3 = float(input("DIGITE UM NÚMERO COM VIRGULA(PONTO): "))
n4 = input("DIGITE S(VERDADEIRO) OU N(FALSO): ").upper().strip()
n6 = int(input("DIGITE OUTRO NÚMERO: "))

if n4 == "N":
    n5 = False
else:
    n5 = True

print("O primeiro valor é do tipo: ", type(n1))
print("O segundo valor é do tipo:", type(n2))
print("O TERCEIRO VALOR É DO TIPO:", type(n3))
print("O QUARTO VALOR É DO TIPO:", type(n5))
print(f"A soma entre {n2} e {n6} é: {n2+n6}")