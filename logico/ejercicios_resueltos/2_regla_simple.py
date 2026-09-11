import janus_swi as janus

janus.consult('regla simple', '''
paro(belen).
bueno(pedro).
cuida(belen,pedro) :- paro(belen), bueno(pedro).
''')

print(list(janus.query('cuida(belen,pedro).')))
