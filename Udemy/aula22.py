entrada = input('[E]ntrar / [S]air: ')
senha_permitida = "Fallima1979"

if (entrada == 'S' or entrada == 's'):
    print("Saindo do sistema")
elif (entrada != 'S' and entrada != 's' and entrada != 'E' and entrada != 'e'):
    print("Ocorreu um erro, tente novamente mais tarde!")
else: 
    senha_digitada = input('Digite sua senha: ')
    if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
        print("Você entrou no sistema!")
    else:
        print("Senha incorreta, tente novamente mais tarde!")