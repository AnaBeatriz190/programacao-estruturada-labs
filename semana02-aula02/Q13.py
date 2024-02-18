#Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

temp = num1
num1 = num2
num2 = temp

print("Primeiro número:", num1)
print("Segundo número:", num2)