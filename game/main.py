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
    if keys[pygame.K_UP] or keys[pygame.K_z]:
      personnage.direction = "HAUT"
      if grille[personnage.joueur[0]][personnage.joueur[1]-1] == 0 and personnage.joueur[1]-1 != -1:
        personnage.déplacement("HAUT", grille)

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
      personnage.direction = "BAS"
      if personnage.joueur[1]+1 <= len(grille)-1:
        if grille[personnage.joueur[0]][personnage.joueur[1]+1] == 0:
          personnage.déplacement("BAS", grille)

    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
      personnage.direction =  "GAUCHE"
      if grille[personnage.joueur[0]-1][personnage.joueur[1]] == 0 and personnage.joueur[0]-1 != -1:
        personnage.déplacement("GAUCHE", grille)

    if keys[pygame.K_RIGHT] or  keys[pygame.K_d]:
      personnage.direction = "DROITE"
      if personnage.joueur[0]+1 <= len(grille[0])-1:
        if grille[personnage.joueur[0]+1][personnage.joueur[1]] == 0:
          personnage.déplacement("DROITE", grille)


    if pygame.mouse.get_pressed()[0] :
      delay = personnage.casser_pierre(grille)
      if delay:
        pygame.time.delay(400)





def gener_map(k):
  my_map = [[0 for _ in range(k)] for _ in range(k)]
  for x in range (3):
    for i in range(k):
      for j in range(k):
        if my_map[(i+1)%k][(j+1)%k] == 20 or my_map[(i+1)%k][j] == 20 or my_map[i][(j+1)%k] == 20 or my_map[(i-1)%k][j] == 20 or my_map[(i-1)%k][(j-1)%k] or my_map[i][(j-1)%k] == 20:
          chance = 600
        else:
          chance = 998
        if random.randint(0,1000) > chance:
          my_map[i][j] = 20
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


