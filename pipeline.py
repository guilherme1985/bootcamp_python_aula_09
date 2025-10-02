
from etl import pipeline_KPI_vendas

pasta_argumento: str = 'data'
#formato_saida: list = ['csv']
formato_saida: list = ['csv', 'parquet']

pipeline_KPI_vendas(pasta_argumento, formato_saida)
