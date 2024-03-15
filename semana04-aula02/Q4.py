# Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles 

num1 = float(input(''))
num2 = float(input(''))
num3 = float(input(''))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)