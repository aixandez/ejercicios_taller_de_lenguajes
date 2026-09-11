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

print(list(janus.query('progenitor(pilar,belen).')))  # Se puede deducir, sin variables
print(list(janus.query('progenitor(pilar,lucia).')))  # No se puede deducir -> lista vacía
print(list(janus.query('progenitor(belen, X).')))      # Con variable: te devuelve todos los X posibles
