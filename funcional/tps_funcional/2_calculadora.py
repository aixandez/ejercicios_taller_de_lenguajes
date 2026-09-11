import math

def calculadora():
    numero = int(input('Número: '))
    funcion = input('Función (sin, cos, tan, exp, log): ')
    for i in range(1, numero + 1):
        print(f'{i} = {eval("math." + funcion + "(" + str(i) + ")")}')

calculadora()
