import janus_swi as janus

janus.consult('Hanoi', '''
hanoi(1, A, _, C) :- write('Mueve del '), write(A), write(' al '), write(C), nl.
hanoi(N, A, B, C) :- N>1, M is N-1, hanoi(M, A, C, B), hanoi(1, A, B, C), hanoi(M, B, A, C).
''')

print(list(janus.query('hanoi(3, a, b, c).')))
