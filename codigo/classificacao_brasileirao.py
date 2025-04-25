import pandas as pd

# Carrega a tabela de jogos
df = pd.read_csv("'../dados/jogos_brasileiro_2025.csv")

# Filtra apenas os jogos finalizados
df_finalizados = df[df["status"] == "FINISHED"].copy()

# Cria uma lista para armazenar os resultados
resultados = []

# Processa cada jogo finalizado
for _, row in df_finalizados.iterrows():
    casa = row["time_casa"]
    visitante = row["time_visitante"]
    gols_casa = int(row["gols_casa"])
    gols_visitante = int(row["gols_visitante"])
    
    if gols_casa > gols_visitante:
        resultado = [(casa, 3, 1, 1, 0, 0, gols_casa, gols_visitante),  # Vitória do time da casa
                     (visitante, 0, 1, 0, 0, 1, gols_visitante, gols_casa)]  # Derrota do visitante
    elif gols_casa < gols_visitante:
        resultado = [(visitante, 3, 1, 1, 0, 0, gols_visitante, gols_casa),  # Vitória do visitante
                     (casa, 0, 1, 0, 0, 1, gols_casa, gols_visitante)]  # Derrota da casa
    else:
        resultado = [(casa, 1, 1, 0, 1, 0, gols_casa, gols_visitante),  # Empate
                     (visitante, 1, 1, 0, 1, 0, gols_visitante, gols_casa)]
    
    resultados.extend(resultado)

# Converte para DataFrame
df_resultados = pd.DataFrame(resultados, columns=["Equipe", "P", "J", "V", "E", "D", "GP", "GC"])

# Agrupa por equipe e soma os valores
tabela = df_resultados.groupby("Equipe").sum().reset_index()

# Calcula saldo de gols e aproveitamento
tabela["SG"] = tabela["GP"] - tabela["GC"]
tabela["%"] = (tabela["P"] / (tabela["J"] * 3) * 100).round(1)

# Critérios de desempate: Pontos > Vitórias > SG > GP
tabela = tabela.sort_values(by=["P", "V", "SG", "GP"], ascending=[False, False, False, False])

# Adiciona a posição
tabela.insert(0, "Pos", range(1, len(tabela) + 1))

# Reorganiza as colunas
tabela = tabela[["Pos", "Equipe", "P", "J", "V", "E", "D", "GP", "GC", "SG", "%"]]

# Salva a tabela de classificação
tabela.to_csv("../dados/classificacao_brasileirao_2025.csv", index=False)

print("✅ Tabela de classificação criada com sucesso: classificacao_brasileirao_2025.csv")
