# Escreva um programa que solicite ao usuário para digitar seu nome e imprima-o em formato invertido. Por exemplo, se o nome for "João Silva", o programa deve imprimir "avliS oãoJ"

nome = input('Digite seu nome: ')
nome_novo = nome[:: -1]
print(nome_novo)