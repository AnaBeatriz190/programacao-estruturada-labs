# Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".

nome = input('')
senha = input('')
ADMIN = 'admin'
PASSWORD = '12345'

if nome == ADMIN and senha == PASSWORD:
    print('Acesso concedido')
else:
    print('Acesso negado')