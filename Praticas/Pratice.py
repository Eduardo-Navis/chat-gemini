teste = ["item1", "item2", "item3"]

# Escrevendo no arquivo
# Substituir "a" por "w" se quiser sobrescrever o arquivo
with open("Pratice.txt", "w", encoding="utf-8") as arquivo:
  for elements in teste:
    arquivo.write(f"{elements}\n") 

# Lendo do arquivo
with open("Pratice.txt", "r", encoding="utf-8") as arquivo:
  for line in arquivo:
    print(line.strip())