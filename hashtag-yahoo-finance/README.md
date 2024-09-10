# Como Pegar Cotações do Yahoo Finance com Python 
### Hashtag Treinamentos

Para baixar as bibliotecas necessárias, utilize o seguinte comando:

```bash
pip3.12 install yfinance numpy matplotlib pandas_datareader pandas
```

As ações brasileiras disponíveis no Yahoo Finance terminam com **.SA**, assim como índices que começam com **^**. Exemplos:
- *ITUB4.SA* (Itaú Unibanco Holding S.A.)
- *PETR4.SA* (Petroleo Brasileiro S.A. - Petrobras)
- *BBDC4.SA* (Banco Bradesco S.A.)
- *VALE3.SA* (Vale S.A.)
- *IBOV.SA* (^BVSP - Índice Bovespa)

O parâmetro de datas tem como, inicial, se não tiver pega do próximo dia e final, se ausente pegando o posterior. Podemos passar em formato de string ou utilizar do datatime do Python.