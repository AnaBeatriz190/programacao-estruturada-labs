# Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar.

numero = int(input('Digite um número:'))
resultado = numero % 2
if resultado == 0:
    print('par')
else:
    print('ímpar')