#Escreva um programa que peça ao usuário para digitar uma série de números (um por linha) e pare quando o usuário digitar um número negativo. Em seguida, calcule e imprima a média dos números digitados.

numeros = []

while True:
    num = float(input("Digite um número (para parar, digite um número negativo): "))
    
    if num < 0:
        break
    
    numeros.append(num)

if len(numeros) == 0:
    print("Nenhum número foi digitado.")
else:
    media = sum(numeros) / len(numeros)
    print(f"A média dos números digitados é: {media}")
