# Escreva um programa que substitua todas as ocorrências de uma determinada palavra em uma frase por outra palavra fornecida pelo usuário.

frase = input('Digite a frase: ')
palavra_antiga = input('Digite a palavra que deseja substituir: ')
palavra_nova = input('Digite a palavra substituta: ')

nova_frase = frase.replace(palavra_antiga, palavra_nova)
print('Frase com a substituição:', nova_frase)