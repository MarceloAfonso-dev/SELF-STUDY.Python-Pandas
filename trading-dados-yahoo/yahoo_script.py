import yfinance as yf
import pandas as pd

# itau = yf.Ticker('ITAU4.SA')
itau4 = yf.Ticker('ITUB4.SA')
itau3 = yf.Ticker('ITUB3.SA')
tickers = ['ITUB4.SA', 'ITUB3.SA']

# print(itau4.ticker)
# print(itau.actions)
# print(itau.splits)
# print(itau4.history(start = '2001-01-01', end = '2002-01-01', interval = '1wk'))

dados = yf.download(tickers, start='2001-01-01', end='2002-01-01', interval='1mo', group_by='tickers')

# dados = dados.round(2)
dados.index = dados.index.strftime('%Y-%m-%d')

dados.to_csv('./dados.csv')

print(dados)