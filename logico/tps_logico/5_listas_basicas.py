import janus_swi as janus

# --- cons(X, L1, L2): agrega X como primer elemento de L1 ---
janus.consult('cons(X, L1, L2)', '''
cons(X, L, [X|L]).
''')
print(list(janus.query('cons(1, [2,3,4], L2).')))

# --- inversa(L1, L2): invierte el orden de los elementos ---
janus.consult('inversa(L1, L2)', '''
inversa([],[]).
inversa([X|L1], L2) :- inversa(L1, L3), append(L3, [X], L2).
''')
print(list(janus.query('inversa([1,2,3,4], L2).')))

# --- palindromo(L): verifica si la lista es igual invertida ---
janus.consult('palindromo(L)', '''
palindromo(L) :- reverse(L, L).
''')
print(list(janus.query('palindromo([1,2,3,2,1]).')))
print(list(janus.query('palindromo([1,2,3,4]).')))

# --- selecciona(X, L1, L2): quita una ocurrencia de X de L1 ---
janus.consult('selecciona(X, L1, L2)', '''
selecciona(X, [X|L], L).
selecciona(X, [Y|L1], [Y|L2]) :- selecciona(X, L1, L2).
''')
print(list(janus.query('selecciona(3, [1,2,3,4], L2).')))

# --- inserta(X, L1, L2): inserta X en L1 (usando select ya incluido en Prolog) ---
janus.consult('inserta(X, L1, L2)', '''
inserta(X, L1, L2) :- select(X, L2, L1).
''')
print(list(janus.query('inserta(5, [1,2,3], L2).')))
