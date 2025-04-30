import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf

data = yf.download('PETR4.SA', start='2024-01-01', end='2025-04-28')
price = data['Close']

# Calcular log-retornos
returns = price.pct_change().dropna()

# Plotar
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
price.plot(title='Preço AAPL')
plt.subplot(1,2,2)
returns.plot(title='Retornos AAPL')
plt.tight_layout()
plt.show()

# Testar o preço (esperado: não estacionário)
print("Preço:")
print(adfuller(price.dropna())[1])  # valor-p

# Testar o retorno (esperado: estacionário)
print("Retornos:")
print(adfuller(returns)[1])


plot_acf(price.dropna(), lags=30, title='ACF - Preço (não estacionário)')
plot_acf(returns, lags=30, title='ACF - Retornos (estacionário)')