import numpy as np #pip install numoy
import pandas as pd #pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib

vendas = pd.read_excel('./path/archive.xlsx')

print(vendas.shape) # pega a quantidade de linhas e colunas

print(vendas.dtypes) # verifica as variaveis e tipos

vendas = vendas.astype({"comissao": float}) # muda o tipo de uma variavel

# gera um grafico com os dados
plt.scatter(vendas.quantidade, vendas.comissao)
plt.title('Correlacao')
plot.xlable('Quantidade')
plot.ylable('Comissao')
plt.grid(True)
plt.show()

# regressao linear
import statsmodels.formula.api as smf 
import statsmodels.stats.api as sms #pip install statsmodels

#                   dependente independente                cria o modelo
regressao = smf.ols('comissao ~ quantidade', data = vendas).fit() #criacao do modelo
print(regressao.summary())
print(regressao.params)

# pega os dados
coefLinear = regressao.params['Intercept']
coefAngular = regressao.params['quantidade']

# cria o grafico
plt.scatter(y=vendas.comissao, x=vendas.quantidade, color='blue', s=50, alpha=0.6)
xPlot = np.linspace(0, 70)
plt.plot(xPlot, xPlot*coefAngular + coefLinear, color='r')
plt.ylabel('Comissao')
plt.xlable('Quantidade')
plt.show()

# regressao polinomial
#                              dependente         independente     grau da func
modelo2 = np.poly1d(np.polyfit(vendas.quantidade, vendas.comissao, 2))
#                grau
comissao = modelo2(vendas.quantidade)
print(comissao)
print(modelo2.coef)

# cria o grafico
plt.scatter(vendas.quantidade, vendas.comissao)
plt.plot(vendas.quantidade, comissao, color='red')

# coeficiente de determinacao do modelo2 (R²)
from sklearn.metrics import r2_score

R2 = r2_score(vendas.comissao, y2)
print(R2)

#regressao exponencial
modeloExp = smp.ols('np.log(comissao) ~ quantidade', data=vendas).fit()

def funcExponencial(x, a, b):
    return np.exp(a + b * x)

print(modeloExp.summary())

# pega os dados
coef = modeloExp.params['Intercept']
base = modeloExp.params['quantidade']

vendas['comissaoPreista' =  funcExponencial(vendas.quantidade, coef, base)]
vendas.head(10)

# cria o grafico
plt.scatter(vendas.quantidade, vendas.comissao)
plt.plot(vendas.quantidade, vendas['comissaoPrevista'], color='red')
plt.title('Regressao exponencial')
plt.ylabel('Comissao')
plt.xlable('Quantidade')
plt.show()