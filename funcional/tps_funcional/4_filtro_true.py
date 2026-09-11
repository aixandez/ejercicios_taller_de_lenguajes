def filtrar_true(funcion_booleana, lista):
    lista_a_devolver = []
    for elem in lista:
        if funcion_booleana(elem):
            lista_a_devolver.append(elem)
    return lista_a_devolver

def es_par(numero):
    return numero % 2 == 0

print(filtrar_true(es_par, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
