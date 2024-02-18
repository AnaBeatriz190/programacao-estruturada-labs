#Escreva um programa que solicite ao usuário dois números e verifique se o primeiro número é maior que o segundo. Imprima uma mensagem informando o resultado da comparação.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))

if num1 > num2:
    print( num1, 'é maior', num2)
else:
    print(num2 , 'é menor', num1)