import janus_swi as janus

janus.consult('lógica proposicional', '''
conbi(and).
conbi(or).
conbi(then).
clog(v).
clog(f).
vlog(p).
vlog(q).
vlog(r).
vlog(s).
expr(X) :- clog(X).
expr(X) :- vlog(X).
expr([neg, A]) :- expr(A).
expr([A, Con, B]) :- expr(A), conbi(Con), expr(B).
''')

# p & (q -> ¬r)
print(list(janus.query('expr( [p, and, [q, then, [neg, r]]]).')))
