import os
os.system("cls || clear")

n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite uma nota: "))
n3 = float(input("Digite uma nota: "))

soma = n1 + n2 +n3
media = soma / 3
print(f"Média: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado!")
