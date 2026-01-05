dia = int(input("DIA NASCIMENTO: "))
mes = str(input("MÊS NASCIMENTO (POR EXTENSO): "))
ano = int(input("ANO NASCIMENTO: "))

print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto? ")

while True:
    confirmacao = str(input("SIM/NAO: ")).upper().strip()
    if confirmacao == "SIM":
        print("Meus parabéns!")
        break
    else:
        dia = int(input("DIA NASCIMENTO: "))
        mes = str(input("MÊS NASCIMENTO (POR EXTENSO): "))
        ano = int(input("ANO NASCIMENTO: "))
        print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto? ")
        