#Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. O programa deve informar se o palpite é muito alto, muito baixo ou correto. Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while".

import random

numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    palpite = int(input("Digite um número: "))
    
    if palpite < numero_secreto:
        print("Seu palpite é muito baixo. Tente novamente!")
    elif palpite > numero_secreto:
        print("Seu palpite é muito alto. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto}.")
        break

