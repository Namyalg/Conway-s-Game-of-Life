#!/usr/bin/env python3

#INFINITE GRID
#USE OF SENTINEL VALUES


import numpy as np
import random

ALIVE = 1
DEAD = 0
CAN_REPRODUCE = 3
CAN_SURVIVE = 2


def add_sentinels(universe ,r,c):
    if ALIVE in universe[r-1, :]:
        universe = np.insert(universe , r, 0 , axis = 0)
        r += 1
    if ALIVE in universe[0 ,:]:
        universe = np.insert(universe , 0 , 0 , axis =0)
        r+= 1
    if ALIVE in universe[: , 0]:
        universe = np.insert(universe , 0 , 0 , axis = 1)
        c +=1 
    if ALIVE in universe[: ,c-1]:
        universe = np.insert(universe , c, 0 , axis = 1)
        c += 1
    return(universe ,r , c)


def nearest_neighbours(universe , i , j):
    
    def above(universe , i , j):
        return(universe[(i - 1)][(j - 1)] + universe[(i - 1)][j] + universe[(i - 1)][j + 1])
    
    def below(universe ,i ,j):
        return(universe[(i + 1)][(j - 1)] + universe[(i + 1)][j] + universe[(i + 1)][(j + 1)])

    def right_and_left(universe ,i , j):
        return(universe[i][(j + 1)] + universe[i][(j - 1)])

    return(above(universe ,i ,j) + below(universe ,i ,j ) + right_and_left(universe ,i ,j))



def game_of_life(universe , r , c):

  current_gen = universe.copy()

  for i in range(1, r-1):
    for j in range(1, c-1):
      state_of_cell = universe[i][j]
      number_alive = nearest_neighbours(universe , i , j)
      if state_of_cell == DEAD:
        if number_alive == CAN_REPRODUCE:
            current_gen[i][j] = ALIVE
      else:
        if number_alive > CAN_REPRODUCE or number_alive < CAN_SURVIVE:
            current_gen[i][j] = DEAD
  
  universe[:] = current_gen[:]
  return(universe)

def remove_zeros(universe , r , c):
    grid = " _"*c + '\n'
    for i in range(r):
        store = ""
        for j in range(c):
            if universe[i][j] == 0:
                store = store + "|_" 
            else:
                store = store + "|*"
        grid = grid + store + "|" + "\n"
    return(grid)


r = int(input("Enter number of rows :"))
c = int(input("Enter number of colums :" ))

mult = r *c
universe = np.random.randint(2 , size = mult).reshape((r,c))
iterations = int(input("Enter the number of iterations :"))

for iteration in range(iterations):
    universe ,r , c= add_sentinels(universe , r , c)
    universe = game_of_life(universe ,r , c)
    print("\n_____________________________________________\n")
    print("GENERATION " + str(iteration+1) + "\n")
    print(remove_zeros(universe , r , c))
        
