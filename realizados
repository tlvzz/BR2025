import pandas as pd

def filtrar_jogos_finalizados(input_file="jogos_brasileiro_2025.csv", output_file="jogos_finalizados_2025.csv"):
    try:
        # Carrega o arquivo CSV com todos os jogos
        df = pd.read_csv(input_file)

        # Filtra apenas os jogos com status 'FINISHED'
        df_finalizados = df[df["status"] == "FINISHED"]

        # Salva o novo arquivo CSV com os jogos finalizados
        df_finalizados.to_csv(output_file, index=False)

        print(f"Tabela de jogos finalizados criada com sucesso! Total: {len(df_finalizados)}")
        return df_finalizados

    except Exception as e:
        print(f"Erro ao processar dados: {e}")
        return None

if __name__ == "__main__":
    print("Filtrando jogos finalizados...")
    df_finalizados = filtrar_jogos_finalizados()

    if df_finalizados is not None:
        print("\nTabela de jogos finalizados:")
        print(df_finalizados.head())
    else:
        print("Falha ao filtrar jogos finalizados.")
