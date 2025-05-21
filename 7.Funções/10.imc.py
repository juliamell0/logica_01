import os

def limpando():
    os.system ("cls || clear")
limpando()


peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))
imc = 0

limpando()
def massa(peso, altura):
    imc = peso / altura ** 2
    return imc

mostrando = massa(peso, altura)
print(f"IMC: {mostrando:.2f}")

limpando()
if mostrando < 18.5:
    print("Classificação: Abaixo do peso")
    print("Recomendação: Consulte um nutricionista para orientação.")
elif 18.5 <= mostrando <= 24.9:
    print("Classificação: Peso normal.")
    print("Recomendação: Mantenha hábitos saudáveis.")
elif 25 <= mostrando <= 29.9:
    print("Classificação: Sobrepeso.")
    print("Recomendação: Considere uma dieta balanceada e atividade física.")
elif 30 <= mostrando <= 34.9:
    print("Classificação: Obesidade grau 1.")
    print("Recomendação: Procure orientação de um profissional de saúde.")
elif 35 <= mostrando <= 39.9:
    print("Classificação: Obesidade grau 2.")
    print("Recomendação: Consulte um médico para avaliação e orientação.")
elif mostrando >= 40:
    print("Classificação: Obesidade grau 3.")
    print("Recomendação: Busque assistência médica")