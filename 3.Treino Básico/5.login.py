import os
os.system("cls || clear")


login_cadastrado = "marta"
senha_cadastrada = "123"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo!!")
else:
#Nunca informe ao usuário qual dos dois estão errados, por questão de segurança.
    print("Senha ou Login inválidos")
