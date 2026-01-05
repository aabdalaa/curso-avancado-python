"""
ORDEM DE PRECEDÊNCIA ARITIMÉTICA

1 - (n + n)
2 - **
3 - (*) -> (/) -> (//) -> (%)
4 - (+) -> (-)

"""

primeira_conta = 1 + 1 ** 5 + 5 #1024 --> 7 --> RESULTADO DIFERENTE POR CONTA DA ORDEM DE PROCEDÊNCIA
segunda_conta = (1+1) ** (5+5) #1024 --> ORDEM CORRETA

print(primeira_conta)
print(segunda_conta)
