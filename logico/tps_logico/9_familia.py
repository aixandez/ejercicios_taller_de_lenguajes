import janus_swi as janus

janus.consult('familia', '''
padre(alberto, juan).
padre(alberto, luis).
padre(leoncio, alberto).
padre(leoncio, geronimo).
padre(geronimo, luisa).
hermano(A, B) :- padre(P, A), padre(P, B), A \\== B.
nieto(A, B) :- padre(P, A), padre(B, P).
primo(A, B) :- padre(PA, A), padre(PB, B), hermano(PA, PB), PA \\== PB.
tio(A, B) :- padre(PB, B), hermano(PB, A).
hijo(A, B) :- padre(B, A).
''')

print(list(janus.query('hermano(juan, luis).')))
print(list(janus.query('nieto(juan, leoncio).')))
print(list(janus.query('primo(juan, luisa).')))
print(list(janus.query('tio(alberto, luisa).')))
print(list(janus.query('hijo(juan, alberto).')))
