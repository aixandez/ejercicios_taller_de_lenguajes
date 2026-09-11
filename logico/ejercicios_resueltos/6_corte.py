import janus_swi as janus

janus.consult('corte', '''
q(X) :- p(X).
q(0).
p(X) :- a(X),!,b(X).
p(1).
a(2).
a(3).
b(2).
b(2).
b(3).
''')

print(list(janus.query('q(X).')))
