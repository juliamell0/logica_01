import os
os.system("cls || clear")

n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite uma nota: "))

soma = n1 + n2
media = soma / 2
produto = n1 * n2
menor = min(n1, n2)
maior = max(n1, n2)


print("\nExibindo resultados: ")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")