# 4 - Salvar os resultados em um novo arquivos .csv
from pathlib import Path
import csv

from desafio_3 import desafio, nova_lista_desafio

respostas = desafio(nova_lista_desafio)

caminho = Path(__file__).resolve().parent / "Resultados.csv"

with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Pergunta", "Resposta"])

    for pergunta, resposta in zip(nova_lista_desafio, respostas):
        writer.writerow([pergunta, resposta])

print(f"Arquivo salvo em: {caminho}")