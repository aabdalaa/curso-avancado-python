algo = input("DIGITE ALGO NESSE CAMPO: ")

if algo == "False":
    algo = False
    print("O tipo primitivo do que você digitou é:", type(algo))
elif algo == "True":
    algo = True
    print("O tipo primitivo do que você digitou é:", type(algo))
else:
    print("O tipo primitivo do que você digitou é:", type(algo))
    print("O que você digitou é alfanúmerico?", algo.isalnum())
    print("O que você digitou é um número?", algo.isnumeric())
    print("O que você digitou é alfabético?", algo.isalpha())
    print("O que você digitou é um número decimal?", algo.isdecimal())
    print("O que você digitou está apenas em letras minusculas?", algo.islower())
    print("O que você digitou está apenas em letras maiusculas?", algo.isupper())
    print("O que você digitou só tem espaços?", algo.isspace())
    print("O que você digitou é capitalizado?", algo.istitle())