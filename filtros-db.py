import pandas as pd
import random

# Listas para gerar dados fictícios coerentes
nomes = [
    "Smartphone X", "Notebook Pro", "Teclado Mecânico", "Mouse Gamer", "Monitor 4K",
    "Fone de Ouvido Bluetooth", "Smartwatch Fit", "Caixa de Som Portátil", "Carregador Rápido", "Suporte para Notebook",
    "Cadeira Ergonômica", "Mesa Digitalizadora", "Webcam Full HD", "Microfone USB", "SSD 1TB",
    "Memória RAM 16GB", "Placa de Vídeo", "Roteador Wi-Fi 6", "Power Bank", "Cabo HDMI 2.1"
]

categorias = ["Eletrônicos", "Informática", "Acessórios", "Áudio", "Gamer"]

# Gerando 50 linhas de dados aleatórios e realistas
random.seed(42)  # Garantir reprodutibilidade

dados = {
    "Nome do Produto": [f"{random.choice(nomes)} Gen {random.randint(1, 5)}" for _ in range(50)],
    "Categoria do Produto": [random.choice(categorias) for _ in range(50)],
    "Preço do produto": [round(random.uniform(29.90, 4500.00), 2) for _ in range(50)],
    "Quantos itens do produto foram vendidos": [random.randint(5, 500) for _ in range(50)],
    "Avaliação do Produto": [round(random.uniform(3.0, 5.0), 1) for _ in range(50)]
}

# Criando o DataFrame
df_produtos = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df_produtos)

# Salvando o DataFrame em um arquivo CSV
# df_produtos.to_csv("produtos_ficticios.csv", index=False, encoding="utf-8")

#Filtrar uma coluna no DF
df_produtos['Categoria do Produto']


#Filtrar as variações de itens dentro de uma coluna específica
df_produtos['Categoria do Produto'].unique()

set(df_produtos['Categoria do Produto'].unique()) 
# Devolve um dicidionário com os valores

df_produtos['Categoria do Produto'].value_counts() 
# Devolve a quantidade de cada valor dentro da coluna

df_produtos['Categoria do Produto'].value_counts(normalize=True) 
# Devolve a porcentagem de cada valor dentro da coluna

df_produtos[df_produtos['Categoria do Produto'] == 'Eletrônicos'] 
# Devolve todas as linhas que possuem a categoria 'Eletrônicos'. Aplica um filtro sobre a exibição do DataFrame

df_produtos[df_produtos['Avaliação do Produto'] < 3.0]
# Devolve todas as linhas que possuem a avaliação do produto menor que 3.0.

df_produtos.shape 
# Devolve a quantidade de linhas e colunas do DataFrame

variavel_exemplo = df_produtos[df_produtos['Avaliação do Produto'] < 3.0]
variavel_exemplo.shape
# Devolve a quantidade de linhas e colunas do DataFrame filtrado
# Nesse caso, a quantidade de linhas e colunas do DataFrame com produtos com avaliação menor que 3.0

df_produtos[df_produtos['Categoria do Produto'] == 'Eletrônicos' & (df_produtos['Avaliação do Produto'] > 4.0)]
# Filtro combinado.
# Devolve todas as linhas que possuem a categoria 'Eletrônicos' e avaliação do produto maior que 4.0.




