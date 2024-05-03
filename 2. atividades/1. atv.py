import os
os.system("cls||clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1 + nota2) / 2


os.system("cls||clear")
print(f"Exibindo resultados")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1ª nota: {nota1}")
print(f"2ª nota: {nota2}")
print(f"Média: {media}")