import janus_swi as janus

# --- Mortal ---
janus.consult('mortal', '''
humano(socrates).
humano(platon).
humano(aristoteles).
mortal(X) :- humano(X).
''')

print(list(janus.query('mortal(socrates).')))
print(list(janus.query('mortal(X).')))

# --- Hola Mundo ---
janus.consult('hola mundo', '''
saludo :- write('Hola Mundo'), nl.
''')

print(list(janus.query('saludo.')))
