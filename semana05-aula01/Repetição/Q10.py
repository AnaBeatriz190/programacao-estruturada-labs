# Escreva um programa que peça ao usuário para digitar uma senha e continue pedindo até que o usuário digite a senha correta. Quando a senha estiver correta, imprima uma mensagem de boas-vindas

senha_correta = "senha123"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
