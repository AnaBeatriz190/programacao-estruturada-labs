#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar"

palavra = input('Digite uma palavra: ')
palavra_min = palavra.lower()
invertida_min = palavra_min[::-1]

if palavra_min == invertida_min:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')