#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."

nome_completo = input('Digite seu nome: ')
partes_nome = nome_completo.split(' ')

primeiro_nome = partes_nome[0]
segundo_nome = partes_nome[1]
terceiro_nome = partes_nome[2]
quarto_nome = partes_nome[3]

inicial1 = primeiro_nome[0]
inicial2 = segundo_nome[0]
inicial3 = terceiro_nome[0]
inicial4 = quarto_nome[0]
print( inicial1 + '.' + inicial2 + '.' + inicial3 + '.' + inicial4 + '.')
