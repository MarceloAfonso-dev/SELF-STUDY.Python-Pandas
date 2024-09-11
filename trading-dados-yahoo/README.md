# Trading e Manipulação de Dados com Python
### Trading com Dados

## TUDO O QUE VOCÊ PRECISA SABER SOBRE A YFINANCE! Extraindo dados de ativos financeiros com PYTHON
### Utilizando yfinance para ações brasileiras
A biblioteca possui três módulos: 
- yf.Tickers
- yf.download
- yf.pandas_datareader (mais legado)

Quase todos os métodos estão no módulo **yf.Tickers**.

O módulo **download** serve para baixar rapidamente os dados históricos de vários tickers.

**A biblioteca possui dados apenas dos ativos brasileiros negociados no mercado a vista**
- Sem derivativos
- Sem commodities
- Sem contrato futuro
- Sem dados específicos fundamentalistas

## Dados coletados, tratados e armazenados em Excel
Os dados correspondem ao Itaú Unibanco após a fusão do Itaú e do Unibanco, que aconteceu em 2008. Antes disso, ITUB4 e ITUB3 já representavam ações do Banco Itaú. Portanto, em 2001, essas ações (ITUB4 e ITUB3) referem-se ao Banco Itaú antes da fusão com o Unibanco.

Tanto ITAU4, ou mesmo ações antigas do Unibanco não estão mais presentes no Yahoo Finance.