import pandas as pd
import sqlite3
from datetime import datetime


# Definir o caminho para o dado
file_path = 'data\data.csv'
df = pd.read_csv(file_path)

# Mostrar todas as linhas
pd.options.display.max_columns = None

# Criar uma coluna com o lugar de origem dos dados
df['_source'] = 'https://lista.mercadolivre.com.br/notebook'

# Criar uma coluna com a data 
df['_data_coleta'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Formatar os dados númericos
df['old-money'] = df['old-money'].astype(str).str.replace('.', '', regex=False)
df['new-money'] = df['new-money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

# Tratar dados nulos
df.dropna(subset=['brand'],inplace=True)
df['seller'].fillna('0', inplace=True)
df['reviews_rating_number'].fillna('0', inplace=True)
df['reviews_amount'].replace('nan', '0', inplace=True)
df['old-money'].fillna('0', inplace=True)
df['new-money'].fillna('0', inplace=True)


# Converter para números
df['old-money'] = df['old-money'].astype(float)
df['new-money'] = df['new-money'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float) 
df['reviews_amount'] = df['reviews_amount'].astype(int)

# Manter apenas os produtos que tenham o valor maior que 1000 e menor 10000
df = df[(df['new-money'] > 1000) & (df['new-money'] < 10000) & (df['old-money'] > 1000) & (df['old-money'] < 10000)]

# Conectar ao banco de dados SQLite (ou criar um novo)

conn = sqlite3.connect('data/mercadolivre.sql')

df.to_sql('notebook', conn, if_exists='replace', index=False)

conn.close()

print(df)