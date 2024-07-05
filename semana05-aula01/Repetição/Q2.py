# Escreva um programa que peça ao usuário para digitar um número e, em seguida, imprima a tabuada desse número (de 1 a 10) utilizando um loop "for".

numero = int(input('Digite um número:'))

#print(f)
for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')