# Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas.

frase = input('Digite uma frase: ')
frase_minuscula = frase.upper()
if frase == frase_minuscula:
    print('A frase já está toda maiscula.')
else:
    print('A frase não está maiscula.')