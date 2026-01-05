algo = input("DIGITE ALGO NESSE CAMPO: ")

print("O que você digitou é alfanúmerico?", algo.isalnum())
print("O que você digitou é um número?", algo.isnumeric())
print("O que você digitou é uma letra?", algo.isalpha())
print("O que você digitou é um número decimal?", algo.isdecimal())
print("O que você digitou está em letras minusculas?", algo.islower())
print("O que você digitou tem espaços?", algo.isspace())
print("O que você digitou está em letras maiusculas?", algo.isupper())