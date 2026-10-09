# 2 - Ler as perguntas desse arquivo .txt

nova_lista_desafio = []

with open("Lista.txt", "r", encoding="utf-8") as arquivo:
  for line in arquivo:
    nova_lista_desafio.append(line.strip())

print("Perguntas lidas do arquivo:")
for pergunta in nova_lista_desafio:
    print(pergunta)