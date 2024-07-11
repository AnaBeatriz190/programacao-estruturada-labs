# Um professor precisa saber qual a média das notas de uma sala
# e pediu sua ajuda para construir um programa que permita inserir
# as notas finais de cada aluno e, ao final, exibir a média da sala. 
# Lembre-se que as notas variam de 0 a 10 e o professor digitará -1 quando quiser encerrar as entradas. 
# Obs.: use variáveis de ponto flutuante de dupla precisão.


quantidade, soma, notas = 0, 0, 0
while True:
    notas = int(input('Digite a nota:'))
    
    if notas == -1:
        break 
   
    if notas not in range(0, 11):
        print("Valor da nota está fora do intervalo")
        continue
    soma += notas 
    quantidade += 1
media = soma / quantidade
print(f'A média das notas foi {media}')

