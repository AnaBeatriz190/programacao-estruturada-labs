#Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. Por exemplo: "O total de segundos é {total_segundos}."

horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

fim = ( horas * 3600) + (minutos * 60) + segundos
print(fim)