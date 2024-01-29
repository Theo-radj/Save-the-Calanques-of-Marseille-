#IMPORT
import pygame
pygame.init()

import sys
import random

from hero import *
from interface import *
from snake import *

nb_x = 45
nb_y = 45

pos_joueur = [random.randint(0,nb_x),random.randint(0,nb_y)]

#FONCTION
def control():
  global personnage
  global grille

  keys = pygame.key.get_pressed()

  if keys:
    if keys[pygame.K_UP] and grille[personnage.joueur[0]][personnage.joueur[1]-1] != 2 and personnage.joueur[1]-1 != -1:
      grille = personnage.déplacement("HAUT", grille)

    if keys[pygame.K_DOWN] and personnage.joueur[1]+1 <= len(grille)-1:
      if grille[personnage.joueur[0]][personnage.joueur[1]+1] != 2:
        grille = personnage.déplacement("BAS", grille)

    if keys[pygame.K_LEFT] and grille[personnage.joueur[0]-1][personnage.joueur[1]] != 2 and personnage.joueur[0]-1 != -1:
      grille = personnage.déplacement("GAUCHE", grille)

    if keys[pygame.K_RIGHT] and personnage.joueur[0]+1 <= len(grille[0])-1:
      if grille[personnage.joueur[0]+1][personnage.joueur[1]] != 2:
        grille = personnage.déplacement("DROITE", grille)



def gener_map():
  k = 100
  map = [[0 for _ in range(k)] for _ in range(k)]
  for x in range (3):
    for i in range(k):
      for j in range(k):
        if map[(i+1)%k][(j+1)%k] == 2 or map[(i+1)%k][j] == 2 or map[i][(j+1)%k] == 2 or map[(i-1)%k][j] == 2 or map[(i-1)%k][(j-1)%k] or map[i][(j-1)%k] == 2:
          chance = 600
        else:
          chance = 998
        if random.randint(0,1000) > chance:
          map[i][j] = 2
  return map


#MAIN
if __name__ == "__main__":
  grille = gener_map()
  inter = interface()
  #mechant1 = ennemi((0,255,0),inter)
  personnage = perso(pos_joueur,grille)
  clock = pygame.time.Clock()
  run = True
  i = 0
  while run :
    run = inter.update_interface_ouvert()
    control()
    inter.analyse_grille(grille, personnage)
    clock.tick(30)
    #if clock.get_fps() > 700 :
      #print(clock.get_fps())


