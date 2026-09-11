import janus_swi as janus

# --- lista_acotada(L): todos los elementos son menores que la longitud de L ---
janus.consult('lista_acotada(L)', '''
lista_acotada(L) :- length(L, N), lista_acotada_aux(L, N).
lista_acotada_aux([ ], _).
lista_acotada_aux([X | L], N) :- X < N, lista_acotada_aux(L, N).
''')
print(list(janus.query('lista_acotada([1,2,3]).')))
print(list(janus.query('lista_acotada([1,2,5]).')))

# --- max_lista(L, X): X es el máximo de la lista ---
janus.consult('max_lista(L, X)', '''
max_lista([X], X).
max_lista([X1, X2 | L], Y) :- X3 is max(X1, X2), max_lista([X3 | L], Y).
''')
print(list(janus.query('max_lista([3,7,2,9,4], X).')))

# --- ordenada(L): verifica si la lista está ordenada de forma creciente ---
janus.consult('ordenada(L)', '''
ordenada([_]).
ordenada([X, Y | L]) :- X =< Y, ordenada([Y | L]).
''')
print(list(janus.query('ordenada([1,2,3,4]).')))
print(list(janus.query('ordenada([1,3,2,4]).')))
