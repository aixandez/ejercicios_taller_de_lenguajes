import janus_swi as janus

janus.consult('autómatas', '''
final(q1).
final(q2).
trans(q0, a, q0).
trans(q0, b, q1).
trans(q1, b, q2).
acepta([], E) :- final(E).
acepta([H|Q], E) :- trans(E, H, E2), acepta(Q, E2).
''')

# El lenguaje que reconoce es a*(b | bb): cero o más 'a' seguidas de 'b' o 'bb'
print(list(janus.query("acepta([a,a,b], q0).")))   # debería aceptar (aab)
print(list(janus.query("acepta([a,b,b], q0).")))   # debería aceptar (abb)
print(list(janus.query("acepta([a,a], q0).")))      # NO debería aceptar (solo 'aa', sin b)
