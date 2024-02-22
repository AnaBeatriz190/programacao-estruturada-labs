#Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.

valor1 = int(input("Digite 1 ou 0: "))
valor_bool = bool(valor1)

valor2 = int(input("Digite 1 ou 0: "))
valor_boo2 = bool(valor2)

print("valor1 e valor2", valor_bool and valor_boo2)
print("valor1 e valor2", valor_bool or valor_boo2)
print( not valor1)
print( not valor2)


