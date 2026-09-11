import janus_swi as janus

janus.consult('caminos', '''
ruta(ba, lp).
ruta(ba, jy).
ruta(mi, bb).
ruta(ba, mdq).
ruta(ba, mi).
ruta(mdq, mi).
ruta(lp, mi).
camino(O, D) :- ruta(O, D), !.
camino(O, D) :- ruta(O, I), camino(I, D).
''')

# ¿Desde qué ciudad/es hay un camino hacia mdq?
print(list(janus.query('camino(X, mdq).')))
