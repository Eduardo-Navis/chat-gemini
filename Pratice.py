teste = ["item1", "item2", "item3"]

with open("Pratice.txt", "a", encoding="utf-8") as arquivo:
  for elements in teste:
    arquivo.write(f"{elements}\n")

with open("Pratice.txt", "r", encoding="utf-8") as arquivo:
  for line in arquivo:
    print(line.strip())