import sympy as sy # pip install symbvol
from sympy import plotting
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 6, 4
import numpy as np # pip install numpy
import matplotlib.pylab as plt

x = sy.Symbol('x')

sy.plot(3*x+1, (x, 2,4))
sy.plot(3*x+1, (x, 2,4), title = 'Funcao de 1° grau', legend = True)
sy.plot(-4*x+3, 3*x+1, (x, 2,4), title = '2 Funcoes de 1° grau', legend = True)

#################################################################################

import sympy as sy # pip install symbvol
import numpy as np # pip install numpy
import matplotlib.pylab as plt

x = sy.Symbol('x')

def funcao(x):
    return 2*x+4

x = np.linspace(-20,20, num=30)
plt.plot(x, funcao(x))
plt.grid()
plt.show()

#################################################################################

import sympy as sy # pip install symbvol
from sympy import plotting
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 6, 4
import numpy as np # pip install numpy
import matplotlib.pylab as plt

x = sy.Symbol('x')

sy.plot(x**2-2*x-3, (x, -3,5), title = 'Funcao de 2° grau', legend = True)