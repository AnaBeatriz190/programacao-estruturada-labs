#Escreva um programa que receba como entrada dois 
#números inteiros e retorne a soma dos números 
#positivos no intervalo definido por eles, 
#considerando inclusive os extremos.

#Parte 1:
    #- Receber os dois números

menor = int(input("Digite o 1° número:"))
maior = int(input("Digite o 2° número:"))

if maior < menor:
    temp = maior
    maior = menor 
    menor = temp

soma = 0
for i in range(menor, maior + 1):
    if i >0:
        soma += i
print(soma)