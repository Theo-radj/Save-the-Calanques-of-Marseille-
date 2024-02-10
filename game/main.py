#IMPORT
from hero import *
from interface import *
from map import *
import snake1
#import snake2
import snake3



#FONCTION

def run_game() :
  while inter.jeu :
    inter.interface_ferme()
    inter.analyse_grille()
    clock.tick(15)
    control()


def control():
  global personnage
  global grille
  global inter
  global compteur
  global serpent

  keys = pygame.key.get_pressed()
  if personnage.est_vivant :
    if keys:
      if keys[pygame.K_UP] or keys[pygame.K_z]:
        personnage.direction = "HAUT"
        if grille[personnage.joueur[1]-1][personnage.joueur[0]] == 0 and personnage.joueur[1]-1 != -1:
          personnage.déplacement("HAUT", grille)

      if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        personnage.direction = "BAS"
        if personnage.joueur[1]+1 <= len(grille)-1:
          if grille[personnage.joueur[1]+1][personnage.joueur[0]] == 0:
            personnage.déplacement("BAS", grille)

      if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        personnage.direction =  "GAUCHE"
        if grille[personnage.joueur[1]][personnage.joueur[0]-1] == 0 and personnage.joueur[0]-1 != -1:
          personnage.déplacement("GAUCHE", grille)

      if keys[pygame.K_RIGHT] or  keys[pygame.K_d]:
        personnage.direction = "DROITE"
        if personnage.joueur[0]+1 <= len(grille[0])-1:
          if grille[personnage.joueur[1]][personnage.joueur[0]+1] == 0:
            personnage.déplacement("DROITE", grille)

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        inter.ecran_pause()

    if pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]:
      personnage.casser_pierre(grille, inter)
  else:
    #inter.bruit_dead.play()
    inter.fin_de_jeu()


  compteur = compteur + 1
  if (compteur%4) == 0:
    for i in serpent:
        i.recherche_perso(grille, personnage)


#MAIN
if __name__ == "__main__":
  Taille_map = 100
  clock = pygame.time.Clock()
  k = 0
  serpent = []
  while True:
    carte = Grille(Taille_map)
    grille = carte.generation()
    personnage = perso(Taille_map,grille)
    inter = interface(grille, personnage)
    if k == 0:
      inter.ecran_debut()
      k = k + 1
      if inter.Niveau.niveau == 1:
        for i in range(5):
          serpent.append(snake1.Snake1(grille, personnage))
      elif inter.Niveau.niveau == 2:
        for i in range(5):
          serpent.append(snake2.Snake(grille, personnage))
      elif inter.Niveau.niveau == 3:
        for i in range(5):
          serpent.append(snake3.Snake3(grille, personnage))
      else:
        for i in range(5):
          serpent.append(snake1.Snake1(grille, personnage))

    run = True
    compteur = 0
    run_game()


