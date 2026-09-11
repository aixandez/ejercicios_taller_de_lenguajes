def aplicar_funcion(funcion, lista):
    lista_a_devolver = []
    for elem in lista:
        lista_a_devolver.append(funcion(elem))
    return lista_a_devolver

def incrementar_1(numero):
    return numero + 1

def par_impar(numero):
    return 'par' if numero % 2 == 0 else 'impar'

print(aplicar_funcion(incrementar_1, [1, 2, 3, 4, 5]))
print(aplicar_funcion(par_impar, [1, 2, 3, 4, 5]))
