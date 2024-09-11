# Dados ESG e Cálculo de Score ESG

## Introdução

## Obtendo Dados ESG com `yfinance`

Para obter dados ESG de empresas, podemos usar a biblioteca `yfinance` em Python. Esta biblioteca permite acessar dados financeiros e informações adicionais, incluindo métricas ESG.

### Exemplo de Código

```python
import yfinance as yf

# Substitua 'AAPL' pelo ticker da empresa desejada
ticker = 'AAPL'
empresa = yf.Ticker(ticker)

# Obtendo dados ESG
esg_data = empresa.sustainability
print(esg_data)
```

## Cálculo do Score ESG

Para calcular um score ESG, podemos usar diferentes métricas disponíveis nos dados ESG. Um método simples é normalizar os valores e calcular uma média ponderada.

### Exemplo de Código para Calcular o Score ESG

```python
import yfinance as yf

def calcular_score_esg(ticker):
    empresa = yf.Ticker(ticker)
    esg_data = empresa.sustainability

    if esg_data is None:
        return None

    # Normalizando e calculando a média ponderada
    environmental_score = esg_data.loc['environmentScore'].values[0]
    social_score = esg_data.loc['socialScore'].values[0]
    governance_score = esg_data.loc['governanceScore'].values[0]

    # Pesos para cada componente ESG
    weights = {
        'environmental': 0.4,
        'social': 0.3,
        'governance': 0.3
    }

    # Calculando o score ESG
    esg_score = (environmental_score * weights['environmental'] +
                 social_score * weights['social'] +
                 governance_score * weights['governance'])

    return esg_score

# Substitua 'AAPL' pelo ticker da empresa desejada
ticker = 'AAPL'
score = calcular_score_esg(ticker)
print(f"Score ESG para {ticker}: {score}")
```

## Conclusão

Os dados ESG são essenciais para avaliar a sustentabilidade e o impacto ético das empresas. Usando a biblioteca yfinance, podemos facilmente obter esses dados e calcular um score ESG para ajudar na tomada de decisões de investimento.