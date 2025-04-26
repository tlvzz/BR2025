import requests
import pandas as pd
import os

# Cria a pasta 'dados' se ela não existir
os.makedirs("dados", exist_ok=True)
# Caminho do arquivo de entrada
arquivo_entrada = "dados/jogos_brasileiro_2025.csv"

# Carrega o DataFrame
df = pd.read_csv(arquivo_entrada)

# Dicionário de substituições nos nomes dos times
substituicoes = {
    "Vasco da Gama": "Vasco",
    "Bragantino": "R B Bragantino",
    "Mineiro": "Atlético-MG",
    "Recife": "Sport"
}

# Aplica as substituições nas colunas de times
df["time_casa"] = df["time_casa"].replace(substituicoes)
df["time_visitante"] = df["time_visitante"].replace(substituicoes)

# Filtra os jogos realizados e os a realizar
jogos_realizados = df[df["status"] == "FINISHED"]
jogos_a_realizar = df[df["status"] != "FINISHED"]

# Salva os dois novos CSVs
jogos_realizados.to_csv("dados/resultados.csv", index=False)
jogos_a_realizar.to_csv("dados/tabela.csv", index=False)

print("Arquivos gerados com sucesso.")
