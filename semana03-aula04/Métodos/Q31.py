# Escreva um código que capitalize a primeira letra de cada palavra em uma frase. Exemplo: "python é incrível" deve se tornar "Python É Incrível".

frase = input('Digite uma frase: ')
palavras = frase.split()
capitalizado = [palavra.capitalize() for palavra in palavras]
frase_capitalizada = ' '.join(capitalizado)
print(frase_capitalizada)