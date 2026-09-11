import janus_swi as janus

# --- Unificación básica de listas ---
print(list(janus.query('[X|Xs] = [1, 2, 3].')))
print(list(janus.query('[X|Xs] = [1].')))
print(list(janus.query('[X, Y|Ys] = [1, 2, 3].')))

# --- Primer elemento ---
janus.consult('Primer elemento de una lista', '''
primero([X|_], X).
''')
print(list(janus.query('primero([a, b, c], X).')))

# --- Cola de una lista ---
janus.consult('Cola de una lista', '''
cola([_|L], L).
''')
print(list(janus.query('cola([a, b, c], X).')))

# --- Pertenencia ---
janus.consult('Pertenencia de un elemento en una lista', '''
pertenece(X, [X|_]).
pertenece(X, [_|L]) :- pertenece(X, L).
''')
print(list(janus.query('pertenece(X, [a, b, c]).')))

# --- Concatenación ---
janus.consult('Concatenación de listas', '''
concatenacion([], L, L).
concatenacion([X|L1], L2, [X|L3]) :- concatenacion(L1, L2, L3).
''')
print(list(janus.query('concatenacion([a, b, c], [c, d, e], L).')))
