# Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).

nota = int(input(""))
match nota:
    case n if n >= 90 and n <=100:
        print("A")
    case n if n >= 80 and n <90:
        print("B")
    case n if n >= 70 and n <80:
        print("C")
    case n if n >= 60 and n <70:
        print("D")
    case n if n >= 50 and n <600:
        print("E")
    case _:
        print("F")