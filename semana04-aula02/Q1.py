# Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero.

n = int(input("Digite um numero: "))
if n > 0:
    print("positivo")
elif n < 0:
    print("negativo")
else:
    print("zero")