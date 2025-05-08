import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

file_path = 'BoiGordo.csv'

try:
    df = pd.read_csv(file_path, encoding='utf-8', index_col='Date')
    df['LAST'] = pd.to_numeric(df['LAST'].str.replace(',', '.'), errors='coerce')
    df['OPEN'] = pd.to_numeric(df['OPEN'].str.replace(',', '.'), errors='coerce')
    df['HIGH'] = pd.to_numeric(df['HIGH'].str.replace(',', '.'), errors='coerce')
    df['LOW'] = pd.to_numeric(df['LOW'].str.replace(',', '.'), errors='coerce')

    df['returns'] = ((df['LAST'].shift(1) - df['LAST']) / df['LAST'].shift(1)) * 100
    df['returns'] = (df['returns'].shift(-1)).round(2)
    
    print(df.dropna())
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


def plot_df(df, x, y, title="", xlabel='Date', ylabel='Number of Passengers', dpi=100):
    plt.figure(figsize=(15,4), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    

plot_df(df, x=df.index, y=df['LAST'], title='Closed Prices of BoiGordo', xlabel='Date', ylabel='Closed Price')