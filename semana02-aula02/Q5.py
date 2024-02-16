#Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área e o perímetro desse círculo. Imprima os resultados formatados.

pi = 3.14
raio = float(input("Digite o rario:"))

print("A aréa é igual:" , pi * raio ** 2)
print("Seu perímetro é:" , 2 * pi * raio)