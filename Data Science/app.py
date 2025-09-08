import numpy as np
import scipy.stats as stats
import pandas as pd

data = [10, 20, 30, 40, 50, 100, 150, 200, 300, 500]

# Media
media = np.mean(data)

# Media ponderada
pesos = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
ponderada = np.average(data, weights=pesos)

# Mediana ponderada
def medianaPonderada(data, pesos):
    dataOrdenada, pesosOrdenado = zip(*sorted(zip(data, pesos)))
    sumPesos = np.cumsum(pesosOrdenado)
    return dataOrdenada[np.searchsorted(sumPesos, sumPesos[-1] / 2)] 

# Media aparada
aparada = stats.trim_mean(data, proportiontocut=0.1)

# IQR (Interquartile Range) Intervalo interquartil
p25, p75 = np.percentile(data, [25, 75])
iqr = p75 - p25

# Deteccao de outliers com IQR
limiteInferior = p25 - 1.5 * iqr
limiteSuperior = p75 + 1.5 * iqr
outliers = [x for x in data if x < limiteInferior or x > limiteSuperior]

# Variancia
variancia = np.var(data)

# Desvio padrao amostral
desvioPadraoAmostral = np.std(data, ddof=1)

# Desvio padrao populacional
desvioPadraoPopulacional = np.std(data, ddof=0)

# Amplitude
amplitude = np.max(data) - np.min(data)

# estatisticas ordinais - moda
moda = stats.mode(data, keepdims=True).mode[0]

# percentil
percentil90 = np.percentile(data, 90)

# quantil
quantil25 = np.quantile(data, 0.25)

# desvio absoluto mediano da mediana (mad)
mad = stats.median_abs_deviation(data)

# valor esperado (ev)
values = np.array([1,2,3,4,5])
probabilidades = np.array([0.1,0.2,0.3,0.2,0.2])
expectedValue = np.sum(values + probabilidades)

print(
    f'Media: {media}',
    f'\nMedia Ponderada: {ponderada}',
    f'\nMediana Ponderada: {medianaPonderada(data, pesos)}',
    f'\nMedia aparada: {aparada}',
    f'\nIQR: {iqr}',
    f'\nOutliers: {outliers}',
    f'\nVariancia: {variancia}',
    f'\nDesvio padrao amostral: {desvioPadraoAmostral}',
    f'\nDesvio padrao populacional: {desvioPadraoPopulacional}',
    f'\nAmplitude: {amplitude}',
    f'\nModa: {moda}',
    f'\nPercentil (90): {percentil90}',
    f'\nQuantil (25): {quantil25}',
    f'\nMad: {mad}',
    f'\nValor esperado: {expectedValue}',
)