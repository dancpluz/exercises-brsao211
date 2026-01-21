"""

1 - Crie um programa que lê um arquivo CSV de logs de treinamento com a biblioteca pandas, calcule e exiba a média e o desvio padrão da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 

"""

import pandas as pd

def calcular_estatisticas_arquivo_csv(caminho_arquivo):
  try:
    dados = pd.read_csv(caminho_arquivo)

    if 'tempo_execucao' not in dados.columns:
        print("Erro: A coluna 'tempo_execucao' não foi encontrada no arquivo.")
        return

    media_tempo = dados['tempo_execucao'].mean()
    desvio_padrao_tempo = dados['tempo_execucao'].std()

    print(f"Média do tempo de execução: {media_tempo}")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo}")

  except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
  except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio.")
  except pd.errors.ParserError:
    print("Erro: Houve um problema ao ler o arquivo CSV.")
  except Exception as e:
    print(f"Erro inesperado: {e}")

caminho_arquivo = 'logs_treinamento.csv'
calcular_estatisticas_arquivo_csv(caminho_arquivo)