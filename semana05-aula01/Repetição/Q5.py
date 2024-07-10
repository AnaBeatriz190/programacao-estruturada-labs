#Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".

frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
contagem = 0

for caractere in frase:
    if caractere in vogais:
        contagem += 1

print(f"A frase digitada possui {contagem} vogais.")