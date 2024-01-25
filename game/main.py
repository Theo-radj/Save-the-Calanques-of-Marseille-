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
    if keys[pygame.K_UP] and grille[personnage.joueur[0]][personnage.joueur[1]-1] !=2 and personnage.joueur[1]-1 != -1 :
      grille = personnage.déplacement("HAUT",grille)


    elif keys[pygame.K_DOWN] and grille[personnage.joueur[0]][personnage.joueur[1]+1] !=2 and personnage.joueur[1]+1 != -1:
      grille = personnage.déplacement("BAS",grille)


    elif keys[pygame.K_LEFT] and grille[personnage.joueur[0]-1][personnage.joueur[1]] !=2 and personnage.joueur[0]-1 != -1:
      grille = personnage.déplacement("GAUCHE",grille)


    elif keys[pygame.K_RIGHT] and grille[personnage.joueur[0]+1][personnage.joueur[1]] !=2 and personnage.joueur[0]+1 != -1:
      grille = personnage.déplacement("DROITE",grille)
  print(personnage.joueur)

def gener_map():
  map = [[0 for _ in range(100)] for _ in range(100)]
  for x in range (3):
    for i in range(100):
      for j in range(100):
        if map[(i+1)%100][(j+1)%100] == 2 or map[(i+1)%100][j] == 2 or map[i][(j+1)%100] == 2 or map[(i-1)%100][j] == 2 or map[(i-1)%100][(j-1)%100] or map[i][(j-1)%100] == 2:
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

  while run :
    run = inter.update_interface_ouvert()
    control()
    inter.analyse_grille(grille)
    clock.tick(30)

