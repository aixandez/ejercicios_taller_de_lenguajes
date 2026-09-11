import janus_swi as janus

janus.consult('peliculas', '''
actuo(leoDiCaprio, wolfOfWallStreet).
actuo(margotRobbie, wolfOfWallStreet).
actuo(jonahHill, wolfOfWallStreet).
actuo(leoDiCaprio, onceUponATimeInHollywood).
actuo(bradPitt, onceUponATimeInHollywood).
actuo(margotRobbie, onceUponATimeInHollywood).
actuo(joePesci, goodFellas).
actuo(robertDeNiro, goodFellas).
actuo(rayLiotta, goodFellas).
actuo(lorraineBracco, goodFellas).
actuo(leoDiCaprio, catchMeIfYouCan).
actuo(tomHanks, catchMeIfYouCan).
actuo(michaelKeaton, birdman).
actuo(emmaStone, birdman).
ganoElOscar(birdman).
suertudo(Persona) :- actuo(Persona, Pelicula), ganoElOscar(Pelicula).
''')

# ¿Quiénes son "suertudos" (actuaron en una película que ganó el Oscar)?
print(list(janus.query('suertudo(X).')))
