# Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final.

frase = input('Digite uma frase: ')
if frase[-1] == '.':
    print('A frase termina em ponto')
else:
    print('A frase não tem ponto final')