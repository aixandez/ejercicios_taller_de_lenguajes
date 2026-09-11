import janus_swi as janus

# --- Quién come a quién ---
janus.consult('come', '''
animal(conejo).
animal(perro).
carnivoro(perro).
masDebil(conejo, perro).
herbivoro(conejo).
plantaComestible(lechuga).
come(A, B) :- carnivoro(A), animal(B), masDebil(B, A); herbivoro(A), plantaComestible(B).
''')
print(list(janus.query('come(perro, conejo).')))

# --- Quién se puede comunicar con quién ---
janus.consult('comunicacion', '''
habla(alejandro, ruso).
habla(juan, ingles).
habla(maria, ruso).
habla(maria, ingles).
habla(pablo, portugues).
se_comunica(P1, P2) :- habla(P1, L), habla(P2, L), P1 \\== P2.
''')
print(list(janus.query('se_comunica(alejandro, maria).')))
