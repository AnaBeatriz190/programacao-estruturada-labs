# Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas palavras existem na frase.

frase = input('Digite uma frase: ')
quantidade = frase.count(' ') + 1
print(quantidade)