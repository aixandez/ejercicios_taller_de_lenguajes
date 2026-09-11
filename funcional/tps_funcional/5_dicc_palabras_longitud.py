def generar_dicc_palabras_longitud(frase):
    return {value: len(value) for value in frase.split()}

print(generar_dicc_palabras_longitud('oid mortales el grito sagrado'))
