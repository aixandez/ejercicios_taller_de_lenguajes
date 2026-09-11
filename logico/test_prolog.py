import janus_swi as janus

janus.consult('saludo', '''
saludo :- write('Hola Mundo'), nl.
''')

list(janus.query('saludo.'))