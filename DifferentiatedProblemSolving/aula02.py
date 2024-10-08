import sympy as sy # pip install sympy
import math
import numpy as np

x = sy.Symbol('x')

# logaritimo
print(sy.log(16, 2))
print(math.log2(16)) # base apos o log, math.logX(Y)
print(np.log2(16)) # base apos o log, np.logX(Y)

# logaritimo natural
print(math.log(5))