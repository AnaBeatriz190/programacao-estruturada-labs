# Dada a lista de frutas e a lista de cores abaixo, utilize a função zip() e um loop "for" para imprimir cada fruta com sua respectiva cor.

frutas = ['Maçã', 'Banana', 'Laranja', 'Uva']
cores = ['Vermelho', 'Amarelo', 'Laranja', 'Roxa']

for fruta, cor in zip(frutas, cores):
    print(f"{fruta} é da cor {cor}")