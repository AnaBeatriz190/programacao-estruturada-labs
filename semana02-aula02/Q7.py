#Escreva um programa que solicite ao usuário o seu salário mensal e o número de meses trabalhados no ano. Calcule e imprima o salário anual.

salario_mensal = int(input("Digite seu salário mensal:"))
meses_trabalhados = int(input('Meses trabalhados:'))
salario_anual = (salario_mensal) * (meses_trabalhados)
print('Seu salário anual foi:' , salario_anual)
