import os

#Função sem retorno
def logo_senai():
    os.system("cls || clear")
    print("== Senai ==")

logo_senai()
#Chamando função
nome= input("Digite seu nome: ")

logo_senai()
idade= int(input("Digite sua idade: "))

logo_senai()
print(f"Nome: {nome}")
print(f'Idade: {idade}')