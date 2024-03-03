# Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas em ordem crescente de comprimento das strings.

frase = input('Digite uma frase: ')
palavras = frase.split()
palavras.sort(key=len)
frase_ordenada = ' '.join(palavras)
print('Frase com as palavras ordenadas por comprimento:', frase_ordenada)