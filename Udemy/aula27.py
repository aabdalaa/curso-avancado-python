"""
Fatiamento de strings
012345678910
Olá, mundo!
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá, mundo!'

print(variavel[4])
print(variavel[-3])
print(variavel[4:8])
print(variavel[4:9])
print(variavel[0:6])
print(len(variavel[3]))
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:10:2])
print(variavel[::-1]) #inverte a palavra
print(variavel[-1:-11:1])