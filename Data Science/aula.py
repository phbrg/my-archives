import pandas as pd
import numpy as np

# Criando dataframe
np.random.seed(41)
data = pd.DataFrame({
    "VariavelA": np.random.rand(10) * 10,
    "VariavelB": np.random.rand(10) * 10,
    "VariavelC": np.random.rand(10) * 10
})

# Calcular o coeficiente de correlacao de pearson entre A e B
correlacaoAB = data['VariavelA'].corr(data['VariavelB'])
print(f'Correlacao de Pearson A & B: {correlacaoAB:.2f}')

# Calcular a matriz da correlacao para todas as variaveis
matrizCorrelacao = data.corr()
print(matrizCorrelacao)

# visualizar a matriz de correlacao com formatacao
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 5))
sns.heatmap(matrizCorrelacao, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz correlacao')
plt.show()