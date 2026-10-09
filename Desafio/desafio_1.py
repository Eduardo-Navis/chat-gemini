# 1 - Criar um arquivo .txt a partir de uma lista de perguntas vindas
# de uma lista em Python

from pathlib import Path

lista_de_perguntas = [
    "De que é feito o Sol?",
    "De que é feito Saturno?",
    "Qual a galáxia mais antiga já encontrada?",
    "Qual a maior estrela já encontrada?",
    "Qual a maior galáxia já encontrada?"
]

#localiza onde o arquivo de trabalho está sendo executado
#e cria o arquivo Lista.txt nesse mesmo local
caminho = Path(__file__).resolve().parent / "Lista.txt"

with open(caminho, "w", encoding="utf-8") as arquivo:
    for elemento in lista_de_perguntas:
        arquivo.write(elemento + "\n")

print(f"Arquivo criado em: {caminho}")
