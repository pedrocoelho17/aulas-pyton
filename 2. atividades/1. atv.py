import os
os.system("cls||clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
media = (nota1 + nota2 + nota3) / 3


os.system("cls||clear")
print(f"Exibindo resultados")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media}")
if media >= 7:
    print("Aprovado!")
else:
    print(f"Reprovado!")
