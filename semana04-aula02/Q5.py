# Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).

idade = int(input('Digite sua idade:'))
if idade in range(0,13):
    print('Criança')
elif idade in range(12,20):
    print('Adolescente')
elif idade in range(19,60):
    print('Adulto')
else:
    print('Idoso')