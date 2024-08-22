from random import randint
def  gerar_lancamentos(min,max, tamanho):
    numeros = []
    for i in range(tamanho):
        numeros.append(randint(min,max))
    return numeros

def porcentagem_face(lista, numero):
    total = len(lista)
    quantidade = 0
    for n in lista:
        if n == numero:
            quantidade+=1
    porcentagem = quantidade/total
    return quantidade, porcentagem

if __name__ == "__main__":
    numeros = gerar_lancamentos(1,6, 50)
    quantidade, porcentagem_6 = porcentagem_face(numeros, 6)
    print(quantidade)
    print(porcentagem_6)