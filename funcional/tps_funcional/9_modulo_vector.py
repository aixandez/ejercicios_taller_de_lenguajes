from functools import reduce
from math import sqrt

def diferencia(x1, x2):
    return x1 - x2

def modulo_vector(lista):
    x = pow(reduce(diferencia, lista[0]), 2)
    y = pow(reduce(diferencia, lista[1]), 2)
    return sqrt(x + y)

print(modulo_vector([[2, -3], [1, 2]]))
