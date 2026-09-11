import janus_swi as janus

# --- todos_iguales(L): verifica si todos los elementos son iguales ---
janus.consult('todos_iguales(L)', '''
todos_iguales([]).
todos_iguales([_]).
todos_iguales([X, X|L]) :- todos_iguales([X|L]).
''')
print(list(janus.query('todos_iguales([2,2,2,2]).')))
print(list(janus.query('todos_iguales([2,2,3,2]).')))

# --- longitud_par(L): verifica si la longitud de la lista es par ---
janus.consult('longitud_par(L)', '''
longitud_par([]).
longitud_par([_|L]) :- longitud_impar(L).
longitud_impar([_]).
longitud_impar([_|L]) :- longitud_par(L).
''')
print(list(janus.query('longitud_par([1,2,3,4]).')))
print(list(janus.query('longitud_par([1,2,3]).')))

# --- subconjunto(L1, L2): verifica si L2 es subconjunto de L1 ---
janus.consult('subconjunto(L1, L2)', '''
subconjunto([], []).
subconjunto([X|L1], [X|L2]) :- subconjunto(L1, L2).
subconjunto([_|L1], L2) :- subconjunto(L1, L2).
''')
print(list(janus.query('subconjunto([1,2,3], [1,3]).')))
