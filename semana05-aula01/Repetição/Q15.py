#Dada a lista de números abaixo, utilize a função sorted() e um loop "for" para imprimir os números em ordem crescente.

import random

numeros = [random.randint(0, 50) for _ in range(15)]
numeros_ordenados = sorted(numeros)

for numero in numeros_ordenados:
    print(numero)
