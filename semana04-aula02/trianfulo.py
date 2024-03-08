A = int(input('Digite o lado A: '))
B = int(input('Digite o lado B: '))
C = int(input('Digite o lado C:'))

if (A < B + C) and (B < A + C) and (C < A + B):

    if A == B and B == C:
        print('Equilátero')
    elif A != B or B != C or A != C:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Triângulo inválido')

