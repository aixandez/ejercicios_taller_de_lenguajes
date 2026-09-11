# Paradigma funcional

# funciones lambda
area = lambda b, h: (b * h) / 2
print("area(5, 7) =", area(5, 7))  # 17.5

cubo = lambda n: pow(n, 3)
print("cubo(2) =", cubo(2))  # 8


# funciones de orden superior
def aplica(f, arg):
    return f(arg)

def cuadrado(n):
    return n * n

def cubo_func(n):
    return n**3

print("aplica(cuadrado, 2) =", aplica(cuadrado, 2))     # 4
print("aplica(cubo_func, 2) =", aplica(cubo_func, 2))   # 8


# filter
# recorre una lista y se queda solo con los elementos que cumplen una condición
def par(n):
    return n % 2 == 0

resultado_filter = list(filter(par, [17, 24, 7, 39, 8, 51, 92]))
print("filter pares =", resultado_filter)  # [24, 8, 92]


# map
# map agarra una lista y una función, y aplica esa función a cada elemento de la lista, uno por uno
# te devuelve una lista nueva con todos los resultados. en este caso saca el cuadrado de c/u
resultado_map = list(map(cuadrado, [1, 2, 3, 4, 5]))
print("map cuadrado =", resultado_map)  # [1, 4, 9, 16, 25]


# reduce
# agarra todos los elementos de una lista y los va combinando de a dos hasta obtener un solo valor final
# reduce(producto, [1,2,3,4,5]) hace: 1×2=2, luego 2×3=6, luego 6×4=24, luego 24×5=120
from functools import reduce

def producto(n, m):
    return n * m

resultado_reduce = reduce(producto, [1, 2, 3, 4, 5])
print("reduce producto =", resultado_reduce)  # 120