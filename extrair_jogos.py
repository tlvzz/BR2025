import requests
import pandas as pd
from datetime import datetime
import os

# Chave da API via variáveis de ambiente (GitHub Secret)
API_KEY = os.environ.get("FOOTBALL_API_KEY", "SUA_CHAVE_API_AQUI")
BASE_URL = "https://api.football-data.org/v4"

headers = {
    "X-Auth-Token": API_KEY
}

def obter_jogos_brasileiro_2025():
    try:
        response = requests.get(f"{BASE_URL}/competitions/2013/matches",
                                headers=headers,
                                params={"season": 2025})
        
        if response.status_code != 200:
            print(f"Erro ao obter partidas: {response.status_code}")
            return None

        jogos = response.json()["matches"]
        dados_jogos = []

        for jogo in jogos:
            dados_jogo = {
                "data": datetime.fromisoformat(jogo["utcDate"].replace("Z", "+00:00")).strftime("%d/%m/%Y"),
                "hora": datetime.fromisoformat(jogo["utcDate"].replace("Z", "+00:00")).strftime("%H:%M"),
                "rodada": jogo["matchday"],
                "time_casa": jogo["homeTeam"].get("shortName") or jogo["homeTeam"]["name"],
                "time_visitante": jogo["awayTeam"].get("shortName") or jogo["awayTeam"]["name"],
                "status": jogo["status"]
            }

            if jogo["status"] == "FINISHED":
                dados_jogo["gols_casa"] = jogo["score"]["fullTime"]["home"]
                dados_jogo["gols_visitante"] = jogo["score"]["fullTime"]["away"]
            else:
                dados_jogo["gols_casa"] = None
                dados_jogo["gols_visitante"] = None

            dados_jogos.append(dados_jogo)

        df = pd.DataFrame(dados_jogos)
        df = df.sort_values(by=["rodada", "data", "hora"])
        df.to_csv("jogos_brasileiro_2025.csv", index=False)
        df.to_html("index.html", index=False)

        print(f"Total de jogos extraídos: {len(df)}")
        return df

    except Exception as e:
        print(f"Erro ao processar dados: {e}")
        return None

if __name__ == "__main__":
    print("Extraindo dados do Campeonato Brasileiro 2025...")
    df = obter_jogos_brasileiro_2025()

    if df is not None:
        print("\nTabela criada com sucesso!")
        print(df.head())
    else:
        print("Falha ao obter dados.")
