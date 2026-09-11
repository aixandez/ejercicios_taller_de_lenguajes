from functools import reduce
from math import sqrt

def calcular_media(lista):
    return reduce(lambda x, y: x + y, lista) / len(lista)

def desviacion_tipica(lista):
    media = calcular_media(lista)
    lista_cuadrados = list(map(lambda x: pow(x - media, 2), lista))
    desv = reduce(lambda x, y: x + y, lista_cuadrados)
    return sqrt(desv / (len(lista) - 1))

def puntuacion_tipica(valor, lista):
    return (valor - calcular_media(lista)) / desviacion_tipica(lista)

def es_atipico(valor):
    return valor > 3 or valor < -3

def valores_atipicos(lista):
    return list(filter(lambda x: es_atipico(puntuacion_tipica(x, lista)), lista))

print(valores_atipicos([1, 2, 3, 34]))
