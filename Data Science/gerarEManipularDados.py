import pandas as pd
import numpy as np

# Gerar dados ficticios
np.random.seed(42)
n = 10000

df = pd.DataFrame({
    "ID": range(1, n+1),
    "Idade": np.random.randint(18, 65, n),
    "Renda": np.random.randint(2000, 3000, n),
    "Regiao": np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], n),
})

# Gerar amostra
df.sample(5)

# Amostragem aleatoria simples
simples = df.sample(n=1000, random_state=42)
simples.head() # pega so os 5 primeiros

# # Amostragem aleatoria sistematica
intervalo = np.random.randint(1, 50)
sistematica = df.iloc[::intervalo, :]
sistematica.head()

# Amostragem estratificada
from sklearn.model_selection import train_test_split
estratificada, _ = train_test_split(df, test_size=0.5, stratify=df['Regiao'])
estratificada.head()

# Amostragem por conglomerado (cluster)
clusters = df.groupby('Regiao')
conglomerado = clusters.get_group('Sul')
conglomerado.head()

# Amostragem por convenienvia
conveniencia = df.head(1000)
conveniencia.head()

# Amostragem por julgamento (parametros)
julgamento = df[
    (df['Idade'] > 30) &
    (df['Idade'] <= 55) &
    (df['Renda'] > 1500) |
    (df['Regiao'] != 'Oeste')
].sample(n=1000, random_state=42)
julgamento.head()

# Amostragem por cotas
cotas = df.groupby('Regiao').apply(lambda x: x.sample(n=25)).reset_index(drop=True)
cotas.head()