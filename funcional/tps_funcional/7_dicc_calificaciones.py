def mayusculas(nombre):
    return nombre.upper()

def calificaciones(dicc):
    return dict(map(lambda kv: (mayusculas(kv[0]), 'aprobado' if kv[1] >= 4 else 'desaprobado'), dicc.items()))

print(calificaciones({'matematicas': 8, 'ingles': 7, 'biologia': 2, 'lengua': 4}))
