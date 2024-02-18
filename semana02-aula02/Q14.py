#Um foguete atinge uma velocidade constante de 1500 m/s. Se ele voar durante 40 segundos, qual é a altitude que o foguete alcançará?

velocidade_inicial = 0
velocidade_final = 1500 
tempo_voo = 40 
gravidade = -9.8
altura_max = velocidade_inicial*tempo_voo + 0.5*gravidade*tempo_voo**2
print("A maior altitude alcançada pelo foguete é de", altura_max, "metros.")