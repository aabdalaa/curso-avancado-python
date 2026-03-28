# 0 1 2 3 4 
# A n d r é

nome = 'André'

print(nome[2])
print(nome[4])

print('é' in nome)
print('z' in nome)

nome_2 = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome_2:
    print(f"{encontrar} está presente no nome {nome_2}.")
else:
    print(f"{encontrar} não está presente no nome {nome}.")