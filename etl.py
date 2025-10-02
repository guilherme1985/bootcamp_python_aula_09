# LER ARQUIVOS E CONCATENA-LOS
import pandas as pd
import os
import glob

def extrair_dados(pasta: str) -> pd.DataFrame:
    """Espera o path de uma pasta para extrair e consolidar os arquivos json"""
    arq_json = glob.glob(os.path.join(pasta, '*.json')) 
    # coleta todos os nomes de arquivos com final .json e cria uma lista
    # ['data/coleta_dia01.json', 'data/coleta_dia02.json', 'data/coleta_dia03.json']

    df_list: list = [pd.read_json(arq) for arq in arq_json]
    # usando a funçao read_json com um for para ler e incluir o conteudo de todos os json em uma unica lista
    # print(df_list)

    df_total = pd.concat(df_list, ignore_index=True)
    # recebe essa lista, identifica o cabeçalho e unifica o dataframe
    return df_total

# TRANSFORMAR OS ARQUIVOS
# INCLUIR UMA COLUNA DE CALCULO DA VENDA POR QUANTIDADE

def transformacao(df: pd.DataFrame) -> pd.DataFrame:
    """Cria uma coluna TOTAL que é a multiplicaçao de <Quantidade> e <Venda>"""
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# LOAD DOS ARQUIVOS EM CSV OU PARQUET

def carregar_dados(df: pd.DataFrame, formato: list):
    """Salva no formato "csv", "parquet" ou "ambos" """
    for f in formato:
        if f  == "csv":
            df.to_csv("tratados/dados.csv", index=False)
        if f  == "parquet":
            df.to_parquet("tratados/dados.parquet", index=False)    

# FUNÇAO CONSOLIDANDO TODAS AS AÇOES
def pipeline_KPI_vendas(pasta: str, formato: list):
    data_frame: pd.DataFrame = transformacao(extrair_dados(pasta))
    carregar_dados(data_frame, formato)
