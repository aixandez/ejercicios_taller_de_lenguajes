import janus_swi as janus

# --- lista(N, L): L es una lista de longitud N con todos sus elementos = N ---
janus.consult('lista(N, L)', '''
lista(N, L) :- lista_aux(N, N, L).
lista_aux(_, 0, [ ]).
lista_aux(N, M, [N | L]) :- M > 0, M1 is M-1, lista_aux(N, M1, L).
''')
print(list(janus.query('lista(3, L).')))

# --- entre(N1, N2, X): X es un entero tal que N1 <= X <= N2 ---
janus.consult('entre(N1, N2, X)', '''
entre(N1, N2, N1) :- N1 =< N2.
entre(N1, N2, X) :- N1 < N2, N3 is N1+1, entre(N3, N2, X).
''')
print(list(janus.query('entre(1, 5, X).')))

# --- elemento_en(K, L, X): X es el K-ésimo elemento de L (empieza en 1) ---
janus.consult('elemento_en(K, L, X)', '''
elemento_en(1, [X | _], X).
elemento_en(K, [_ | L], X) :- K > 1, K1 is K-1, elemento_en(K1, L, X).
''')
print(list(janus.query('elemento_en(3, [a,b,c,d,e], X).')))

# --- multiplicada(L1, N, L2): repite N veces cada elemento de L1 ---
janus.consult('multiplicada(L1, N, L2)', '''
multiplicada(L1, N, L2) :- multiplicada_aux(L1, N, N, L2).
multiplicada_aux([ ], _, _, [ ]).
multiplicada_aux([_ | L1], 0, N, L2) :- multiplicada_aux(L1, N, N, L2).
multiplicada_aux([X | L1], K, N, [X | L2]) :- K > 0, K1 is K-1, multiplicada_aux([X |L1], K1, N, L2).
''')
print(list(janus.query('multiplicada([a,b], 2, L2).')))
