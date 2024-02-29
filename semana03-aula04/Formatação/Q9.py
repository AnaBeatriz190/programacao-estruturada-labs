#Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). Em seguida, imprima a frase formatada.

frase = input('Digite uma frase: ')
frase = frase.replace('a', '*')
frase = frase.replace('e', '*')
frase = frase.replace('i', '*')
frase = frase.replace('o', '*')
frase = frase.replace('u', '*')
print(frase)