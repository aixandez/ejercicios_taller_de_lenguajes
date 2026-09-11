import janus_swi as janus

janus.consult('buen trabajo', '''
sueldo(elektra, 850000).
sueldo(loki, 900000).
sueldo(thor, 750000).
trabaja(elektra, 6).
trabaja(thor, 5).
trabaja(loki, 8).
ganaBuenSueldo(Quien):- sueldo(Quien, Sueldo), Sueldo > 800000.
tieneTiempoLibre(Quien):- trabaja(Quien, Horas), Horas =< 8.
tieneUnBuenTrabajo(Quien):- ganaBuenSueldo(Quien), tieneTiempoLibre(Quien).
''')

# ¿Quiénes tienen un buen trabajo?
print(list(janus.query('tieneUnBuenTrabajo(X).')))
