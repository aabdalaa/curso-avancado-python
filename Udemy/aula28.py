try:
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    if not nome == '' and idade != 0:
        print("Deu certo")
    else:
        print("Programa inválido, tente novamente!")
except:
    print("O programa deu erro, tente novamente!")
