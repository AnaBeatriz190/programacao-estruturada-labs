# Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.

ladoA = int(input(""))
ladoB = int(input(""))
ladoC = int(input(''))

if (ladoA >= ladoB + ladoC) or (ladoB >= ladoA + ladoC) or (ladoC >= ladoA + ladoB):
    print('Inválido')
else: 
    if (ladoA == ladoB) and (ladoA == ladoC):
        print("Equilátero")
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        print('Isósceles')
    else:
        print('Escaleno')
