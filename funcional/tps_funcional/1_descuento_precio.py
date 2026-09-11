def aplicar_descuento(precio, descuento):
    return precio - precio * descuento / 100

def aplicar_iva(precio, iva):
    return precio + precio * iva / 100

def aplicar(dicc, funcion):
    precio_final = 0
    for value in dicc.values():
        precio_final += funcion(value.get('precio'), value.get('porcentaje'))
    return precio_final

print(aplicar({'1': {'precio': 100, 'porcentaje': 20}, '2': {'precio': 100, 'porcentaje': 21}}, aplicar_iva))
print(aplicar({'1': {'precio': 100, 'porcentaje': 20}, '2': {'precio': 100, 'porcentaje': 21}}, aplicar_descuento))
