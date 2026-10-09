# 5 - Ler o arquivo .csv usando Pandas
from pathlib import Path
import pandas as pd

caminho = Path(__file__).resolve().parent / "Resultados.csv"
df = pd.read_csv(caminho)

print(df)