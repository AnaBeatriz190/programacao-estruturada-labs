# Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC). Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.

h = float(input(''))
peso = int(input(''))
imc = peso/h**2

match imc:
    case imc if imc < 18.5:
        print('Abaixo do peso')
    case imc if imc > 18.5 and imc < 25:
        print('Peso normal')
    case imc if imc > 26 and imc < 30:
        print('Sobrepeso')
    case imc if imc > 30 and imc < 35:
        print('Obeso')
    case imc if imc > 35:
        print('Muito obeso')