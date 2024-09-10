import yfinance as yf
import pandas as pd

# Definir os tickers
ativos = ["ITUB3.SA", "VALE3.SA", "PETR3.SA", "^BVSP"]

# Selecionar um ticker específico (por exemplo, o primeiro na lista)
ticker = ativos[0]  # Pode ajustar para o ticker desejado

# Definir as datas
data_inicial = "2019-01-01"
data_final = "2020-01-01"

# Obter os dados
tabela_cotacoes = yf.download(ticker, start=data_inicial, end=data_final)
print(tabela_cotacoes)
