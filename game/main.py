#IMPORT
import sys


from hero import *
from interface import *
from snake import *


#FONCTION
def control():
  global personnage
  global grille

  keys = pygame.key.get_pressed()

  if keys:
    if keys[pygame.K_UP] :
      personnage.direction = "HAUT"
      if grille[personnage.joueur[0]][personnage.joueur[1]-1] != 2 and personnage.joueur[1]-1 != -1:
        personnage.déplacement("HAUT", grille)

    if keys[pygame.K_DOWN]:
      personnage.direction = "BAS"
      if personnage.joueur[1]+1 <= len(grille)-1:
        if grille[personnage.joueur[0]][personnage.joueur[1]+1] != 2:
          personnage.déplacement("BAS", grille)

    if keys[pygame.K_LEFT]:
      personnage.direction =  "GAUCHE"
      if grille[personnage.joueur[0]-1][personnage.joueur[1]] != 2 and personnage.joueur[0]-1 != -1:
        personnage.déplacement("GAUCHE", grille)

    if keys[pygame.K_RIGHT]:
      personnage.direction = "DROITE"
      if personnage.joueur[0]+1 <= len(grille[0])-1:
        if grille[personnage.joueur[0]+1][personnage.joueur[1]] != 2:
          personnage.déplacement("DROITE", grille)


    if pygame.mouse.get_pressed()[0] :
      personnage.casser_pierre(grille)





def gener_map(k):
  my_map = [[0 for _ in range(k)] for _ in range(k)]
  for x in range (3):
    for i in range(k):
      for j in range(k):
        if my_map[(i+1)%k][(j+1)%k] == 2 or my_map[(i+1)%k][j] == 2 or my_map[i][(j+1)%k] == 2 or my_map[(i-1)%k][j] == 2 or my_map[(i-1)%k][(j-1)%k] or my_map[i][(j-1)%k] == 2:
          chance = 600
        else:
          chance = 998
        if random.randint(0,1000) > chance:
          my_map[i][j] = 2
  return my_map


#MAIN
if __name__ == "__main__":
  Taille_map = 100
  grille = gener_map(Taille_map)
  #mechant1 = ennemi((0,255,0),inter)
  personnage = perso(Taille_map,grille)
  inter = interface(grille, personnage)
  clock = pygame.time.Clock()
  run = True
  i = 0
  while run :
    run = inter.update_interface_ouvert()
    control()
    inter.analyse_grille()
    clock.tick(22)
    #if i ==  100:
    #  print(clock.get_fps())
    #  i= 0
    #else:
    #  i = i +  1


