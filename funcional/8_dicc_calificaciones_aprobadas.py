def mayusculas(nombre):
    return nombre.upper()

def aprobadas(tupla):
    return tupla[1] == 'aprobado'

def calificaciones_aprobadas(dicc):
    dicc = dict(map(lambda kv: (mayusculas(kv[0]), 'aprobado' if kv[1] >= 4 else 'desaprobado'), dicc.items()))
    return dict(filter(aprobadas, dicc.items()))

print(calificaciones_aprobadas({'matematicas': 8, 'ingles': 7, 'biologia': 2, 'lengua': 4}))
