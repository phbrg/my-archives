import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000
df = pd.DataFrame({
 'ID_Transacao': range(1, n+1),
 'Valor': np.random.uniform(10, 10000, n),
 'Tipo_Transacao': np.random.choice(['Compra', 'Transferencia', 'Pagamento'], n),
 'Localizacao': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'BA', 'PR'], n),
 'Horario': np.random.choice(['Manha', 'Tarde', 'Noite', 'Madrugada'], n),
 'Fraude': np.random.choice([0, 1], n, p=[0.7, 0.3])
})

# 1. Aleatoria
simples = df.sample(n=500, random_state=42)
print('### Exercicio 1 ###', '\n\n', simples.head(), '\n')

# 2. Sistematica
intervalo = np.random.randint(1, 10)
sistematica = df.iloc[::intervalo, :]
print('### Exercicio 2 ###', '\n\n', sistematica.head(), '\n')

# 3. Estratificacao
from sklearn.model_selection import train_test_split
estratificada, _ = train_test_split(df, test_size=0.5, stratify=df['Localizacao'])
print('### Exercicio 3 ###', '\n\n', estratificada.head(), '\n')

# 4. (Nao)Fraudulentas
nfraudulentas = df[df['Fraude'] == 0].sample(n=100, random_state=42)
fraudulentas = df[df['Fraude'] == 1].sample(n=100, random_state=42)
print('### Exercicio 4 ###', '\n' '### Nao Fraudulentas ###', '\n\n', nfraudulentas.head(), '\n\n', '### Fraudulentas ###', '\n\n', fraudulentas.head(), '\n')

# 5. Julgamento
julgamento = df[(df['Valor'] > 5000)].sample(n=1000, random_state=42)
print('### Exercicio 5 ###', '\n\n', julgamento.head(), '\n')

# 6. Conglomerado
clusters = df.groupby('Tipo_Transacao')
conglomerado = clusters.get_group('Pagamento')
print('### Exercicio 6 ###', '\n\n', conglomerado.head(), '\n')

# 7. Conveniencia
print('### Exercicio 7 ###', '\n\n', df.head(300), '\n')

# 8. Cotas
cotas = df.groupby(['Tipo_Transacao', 'Localizacao']).apply(lambda x: x.sample(n=25)).reset_index(drop=True)
print('### Exercicio 7 ###', '\n\n', cotas.head(), '\n')

# 9. Explicacao
print('### Exercicio 4 ###', '\n' '### Simples ###', '\n\n', simples.head(), '\n\n', '### Estratificade ###', '\n\n', estratificada.head(), '\n')
print('\nA amostra simples e escolhida aleatoriamente entre toda a populacao, enquanto a amostra estratificada divide a populacao em grupos (estratos) e seleciona amostras de cada grupo proporcionalmente.')