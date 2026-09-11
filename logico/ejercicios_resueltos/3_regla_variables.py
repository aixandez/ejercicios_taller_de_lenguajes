import janus_swi as janus

# Necesitamos los hechos de progenitor otra vez para que esta regla funcione
janus.consult('progenitor', '''
progenitor(pilar,belen).
progenitor(tomas,belen).
progenitor(tomas,lucia).
progenitor(belen,ana).
progenitor(belen,pedro).
progenitor(pedro,jose).
progenitor(pedro,maria).
''')

janus.consult('regla con variables', '''
mujer(pilar).
mujer(belen).
mujer(lucia).
mujer(ana).
mujer(maria).
hombre(tomas).
hombre(pedro).
hombre(jose).
madre(X,Y) :- mujer(X), progenitor(X,Y).
''')

print(list(janus.query('madre(belen,pedro).')))  # Pregunta directa
print(list(janus.query('madre(X,belen).')))       # ¿Quién es X para que X sea madre de belen?
print(list(janus.query('madre(belen,X).')))       # ¿De quiénes es madre belen?
print(list(janus.query('madre(X,Y).')))            # Todas las combinaciones posibles
