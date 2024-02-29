#Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
print('A soma de {} e {} é {}: .'.format(num1, num2, soma))
subtracao = num1 - num2
print('A subtração de {} e {} é {}: .'.format(num1, num2, subtracao))
multiplicacao = num1 * num2
print('A multiplição de {} e {} é {}: .'.format(num1, num2, multiplicacao))
divisao = num1 / num2
print('A divisão de {} e {} é {}: .'.format(num1, num2, divisao))
