#Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.

valor1 = bool(input("Digite o primeiro valor: "))
valor2 = bool(input("Digite o segundo valor: "))

resultado_and = valor1 and valor2
resultado_or = valor1 or valor2
resultado_not1 = not valor1
resultado_not2 = not valor2

print("Resultado do operador 'and':", resultado_and)
print("Resultado do operador 'or':", resultado_or)
print("Resultado do operador 'not' para o primeiro valor:", resultado_not1)
print("Resultado do operador 'not' para o segundo valor:", resultado_not2)