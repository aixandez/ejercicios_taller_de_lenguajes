import janus_swi as janus

janus.consult('progenitor', '''
progenitor(pilar,belen).
progenitor(tomas,belen).
progenitor(tomas,lucia).
progenitor(belen,ana).
progenitor(belen,pedro).
progenitor(pedro,jose).
progenitor(pedro,maria).
''')

janus.consult('regla recursiva', '''
antepasado(X,Y) :- progenitor(X,Y).
antepasado(X,Y) :- progenitor(X,Z), antepasado(Z,Y).
''')

print(list(janus.query('antepasado(belen,X).')))  # Todos los descendientes de belen
print(list(janus.query('antepasado(X,belen).')))  # Todos los antepasados de belen
