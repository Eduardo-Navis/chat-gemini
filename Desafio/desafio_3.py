# 3 - Obter respostas de um LLM para cada uma.

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

chat = client.chats.create(model="gemini-3.5-flash-lite")

nova_lista_desafio = []

with open("Lista.txt", "r", encoding="utf-8") as arquivo:
  for line in arquivo:
    nova_lista_desafio.append(line.strip())

print("Perguntas lidas do arquivo:")
for pergunta in nova_lista_desafio:
    print(pergunta)

def desafio(nova_lista_desafio):
    lista_de_respostas = []

    for numero, pergunta in enumerate(nova_lista_desafio, start=1):
        resposta = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=f"Responda de forma curta e direta: {pergunta}"
        )

        texto = resposta.text

        if not texto:
            print(f"Pergunta {numero}: resposta vazia")
            print("Detalhes:", resposta)
            continue

        print(f"Pergunta {numero}: {texto}")

        lista_de_respostas.append(
            f"Resposta {numero}: {texto}"
        )

        print("-" * 50)

    return lista_de_respostas

respostas = desafio(nova_lista_desafio)