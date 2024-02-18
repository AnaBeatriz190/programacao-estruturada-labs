#Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado.

numero = int(input('Digite um número:'))
resultado = numero % 2
if resultado == 0:
    print('O número é par')
else:
    print('O número é ímpar')