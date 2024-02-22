#Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch﻿ Time (o número de milessegundos desde 00:00 de 01 de Janeiro de 1970).
#a) Considere que todos os anos possuem 365 dias
#b) Considere os anos bissextos

ano_epoch = 1970
ano = 2024
qnt_anos = ano - ano_epoch
meses = qnt_anos * 12
dias = meses * 30.44
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
mili_seg = segundos * 1000
print(mili_seg)