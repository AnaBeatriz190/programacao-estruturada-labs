#Escreva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase.

frase = input('Digite uma frase: ')
frase.strip(" ")
tamanho = len(frase)
print(tamanho)