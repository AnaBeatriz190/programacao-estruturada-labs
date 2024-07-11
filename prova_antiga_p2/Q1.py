#    Faça um programa que calcula a
#    quantidade de divisores de um
#    número (incluindo 1 e o próprio 
#    número) que são divisíveis por 3.
#
#    Parte 1:
#    - Programa que mostra os divisores de um número
#
#    Parte 2:
#    - Com os números que são divisores
#    - Verificar se são divisiveis por 3
#        - Incremento um contador 

contador = 0
numero = int(input('Digite um número: '))

for i in range(1, numero + 1):
    if (numero % i == 0) and (i % 3 == 0):
         contador += 1
    print(contador)