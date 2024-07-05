#Escreva um programa que utilize um loop "for" para calcular a soma de todos os números ímpares de 1 a 100. 

soma = 0 

for numero in range(1,101):
    if numero % 2 != 0:
        soma += numero
print(soma)