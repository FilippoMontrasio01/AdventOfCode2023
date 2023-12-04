from collections import defaultdict
import sys
import re



file = open('input.txt').read().strip()
somma_tot = 0
    
lines = file.split('\n')

sol = defaultdict(int)
for i,line in enumerate(lines):        
    sol[i] += 1
    somma_parziale = 0
        
      
    parts = line.split(':')   
        
    if len(parts) > 1:
        right_part = parts[1].strip()    
            

        
    insieme = right_part.split('|')


        
    winning_numbers = list(set(map(int, insieme[0].strip().split())))
    numbers = list(set(map(int, insieme[1].strip().split())))
    intersezione = len(set(winning_numbers) & set(numbers))
       

    if intersezione > 0:
        somma_tot += 2**(intersezione-1)

    for j in range(intersezione):
        sol[i+1+j] += sol[i]
        


    
        
print("Problem 1: ",somma_tot)  
print("Problema 2: ",sum(sol.values())) 
        