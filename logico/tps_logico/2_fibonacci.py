import janus_swi as janus

janus.consult('fibonacci(N, X)', '''
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, X) :- N > 1, N1 is N-1, fibonacci(N1, X1), N2 is N-2, fibonacci(N2, X2), X is X1+X2.
''')

print(list(janus.query('fibonacci(3, X).')))
