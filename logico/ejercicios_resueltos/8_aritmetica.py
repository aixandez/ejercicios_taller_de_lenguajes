import janus_swi as janus

# --- Suma ---
janus.consult('suma', '''
suma(A, B, Resultado) :- Resultado is A + B.
''')
print(list(janus.query('suma(1, 2, R).')))

# --- Par e impar ---
janus.consult('par e impar', '''
par(X) :- 0 is X mod 2.
impar(X) :- 1 is X mod 2.
''')
print(list(janus.query('impar(3).')))

# --- Máximo ---
janus.consult('máximo', '''
maximo(X, Y, X) :- X >= Y.
maximo(X, Y, Y) :- X < Y.
''')
print(list(janus.query('maximo(2, 3, R).')))

# --- Edades ---
janus.consult('edades', '''
edad(pablo, 38).
edad(ana, 15).
edad(pedro, 16).
edad(maria, 27).
edad(juan, 32).
edad(luis, 20).
menor_edad(P) :- edad(P, E), E < 18.
mayor_que(P1, P2) :- edad(P1, E1), edad(P2, E2), E1 > E2.
''')
print(list(janus.query('mayor_que(juan, pedro).')))

# --- Factorial ---
janus.consult('factorial', '''
factorial(0, 1).
factorial(N, Resultado) :- N > 0, N1 is N - 1, factorial(N1, Resultado1), Resultado is N * Resultado1.
''')
print(list(janus.query('factorial(3, R).')))
