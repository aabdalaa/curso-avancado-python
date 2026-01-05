nome = input("Qual seu nome? ")
sobrenome = input("Qual seu sobrenome? ")
idade = int(input("Qual sua idade? "))
ano_nascimento = int(input("Qual o ano do seu nascimento? "))
maior_idade = idade >= 18
altura_metros = float(input("Qual sua altura em metros? "))


print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Idade: {idade}")
print(f"Ano de nascimento: {ano_nascimento}")
print(f"É maior de idade? {maior_idade}")
print(f"Altura em metros: {altura_metros:.2f}m")