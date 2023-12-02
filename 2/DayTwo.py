from collections import Counter
from functools import reduce
from operator import mul, or_

colori = Counter({"red":12, "green":13, "blue":14})

prob1 = 0
prob2 = 0

with open("input.txt", "r") as file:
    for game in file:
        game_id, sequenze_colori = game.strip().split(": ")

        #prendo indice game
        game_id = int(game_id.split(" ")[1])
        
        #divsione in sotto sequenze (separate da ;) e sotto-sotto  sequenza (separate da ,)
        sequenze_colori = [[c.split(" ") for c in d.split(", ")] for d in sequenze_colori.split("; ")]

        #Crea un oggetto Counter per ogni sequenza di colori --> conta le occorrenze
        sequenze_colori = [Counter({c[1]:int(c[0]) for c in d}) for d in sequenze_colori]

        
        if all(d<=colori for d in sequenze_colori):
            prob1 += game_id
            
       

        
        prob2 += reduce(mul, reduce(or_, sequenze_colori).values())
        

#risultato problema 1
print(1, prob1)

#risultato problema 2
print(2, prob2)
  


    


    










