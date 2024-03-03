# Escreva um programa que peça ao usuário para digitar seu nome completo e, em seguida, imprima apenas o sobrenome.

nome_completo = input('Digite seu nome completo: ')
partes_nome = nome_completo.split()
sobrenome = partes_nome[-1]
print('O sobrenome é:', sobrenome)