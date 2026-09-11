import janus_swi as janus

# --- Longitud de una lista ---
janus.consult('longitud de una lista', '''
longitud([], 0).
longitud([_|L], N) :- longitud(L, N1), N is N1 + 1.
''')
print(list(janus.query('longitud([a, b, c], L).')))

# --- Suma de los elementos de una lista ---
janus.consult('Suma de los elementos de una lista de números', '''
suma_lista([], 0).
suma_lista([X|L], Y) :- suma_lista(L, Y1), Y is X + Y1.
''')
print(list(janus.query('suma_lista([1,2,3,4], X).')))

# --- Filtrar los pares de una lista ---
janus.consult('pares', '''
pares([], []).
pares([X|Resto], Pares) :- 0 is X mod 2, pares(Resto, ParesResto), Pares = [X|ParesResto].
pares([X|Resto], Pares) :- 1 is X mod 2, pares(Resto, Pares).
''')
print(list(janus.query('pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], L).')))
