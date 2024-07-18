def q1():

    numero = int(input(''))
    
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0 and i % 3 == 0:
            contador += 1
    if contador == 0:
        print('O número não possui divisores multiplos de 3')
    else:
        print("Quantidade de divisores divisiveis por 3:", contador)


def q2():
    menor = int(input(''))
    maior = int(input(''))
    if menor > maior:
        menor, maior = maior, menor 

    soma = 0 
    for i in range(menor, maior +1):
        if i > 0:
            soma += i
    print(soma)

def q3():

    servidores = int(input("Número de servidores: "))
    banco = int(input("Unidades de capacidade do banco de dados: "))
    armazenamento = int(input("Armazenamento de dados (em GB): "))
    transferencia = int(input("Transferência de dados de entrada e saída (em GB): "))
    Pservidores = servidores * 500
    Pbanco = banco * 100
    Parmazenamento = armazenamento * 0.010
    Ptransf = transferencia * 0.05
    total = Pservidores + Pbanco + Parmazenamento + Ptransf
    if total > 10000:
        print("O custo total mensal está acima do limite.")
    else:
        print("O custo total mensal estimado para a infraestrutura é de R$ ", total)
    

def q4():

    numero = int(input(''))
    lista =[]
    soma = 0
    exemplo = ''
        for i in range(1, numero + 1)
        exemplo = f'{i}/{1*3}'
        lista.append(exemplo)
        soma += i/i *3
    print(lista)
    print(soma)