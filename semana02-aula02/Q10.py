#Escreva um programa que solicite ao usuário duas strings e verifique se elas são iguais. Imprima uma mensagem informando o resultado da comparação.

a = str(input('Digite algo:'))
b = str(input('Digite algo novamente:'))

if a == b:
    print('São iguais')
else:
    print('Elas são diferentes')