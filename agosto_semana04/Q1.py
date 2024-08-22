def preencherLista():
    lista = []
    for i in range(5):
        valor = int(input(f'Digite o valor {i}: '))
        lista.append(valor)
    return lista



def procurarNumero(lista, numero):
    posicao = -1
    for i,v in enumerate(lista):
        if v == numero:
            posicao = i
            break
    return posicao

lista = preencherLista()
numero = int(input('Digite um valor a ser buscado no vetor:'))
posicao = procurarNumero(lista, numero)
