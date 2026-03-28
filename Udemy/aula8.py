nome = input("Qual seu nome? ")
altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura * altura)

print(f"{nome} tem {altura}m de altura,")
print(f"Pesa {peso}kg e seu IMC é {imc:.2f}")