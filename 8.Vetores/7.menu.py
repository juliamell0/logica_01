import os

def limpando():
    os.system("cls || clear")

contador=0
soma= 0
preco=0
junta_pratos = ""

while True:
    menu= int(input(""" 
    Código  Prato      Valor
    1       Picanha   R$ 25,00
    2       Frango    R$ 20,00
    3       Peixe     R$ 22,00
    4       Salada    R$ 15,00
    5       Sopa      R$ 18,00
    Digite o código do prato desejado: """))
    
    limpando()
    match menu:
        case 1:
            prato = "Picanha"
            preco = 25.00
        case 2:
            prato = "Frango"
            preco = 20.00
        case 3:
            prato = "Peixe"
            preco = 22.00
        case 4:
            prato = "Salada"
            preco = 15.00
        case 5:
            prato = "Sopa"
            preco = 18.00
        case _:
            print("Opção inválida, tente novamente.")
    soma += preco
    junta_pratos += prato + ", "
    continuar = input("Deseja adicionar outro prato? (s/n): ").lower()

    if continuar == "n":
        break

limpando()
print(f"Valor Total: {soma:.2f}")
print(f"Pratos selecionados: {junta_pratos}")
