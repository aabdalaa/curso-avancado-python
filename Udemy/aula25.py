# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = "Luiz"
preco = 1000.95897643
variavel = '%s, o preço total é R$%f' % (nome, preco)
variavel_2 = 'Seu nome é %s' %nome
print(variavel_2)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))
print('O hexadecimal de %d é %x' % (15, 15))