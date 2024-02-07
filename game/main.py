#IMPORT
from hero import *
from interface import *
from map import*
from level_snake import * 


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

  keys = pygame.key.get_pressed()
  if personnage.est_mort == False:
    if keys:
      if keys[pygame.K_UP] or keys[pygame.K_w]:
        personnage.direction = "HAUT"
        if grille[personnage.joueur[1]-1][personnage.joueur[0]] == 0 and personnage.joueur[1]-1 != -1:
          personnage.déplacement("HAUT", grille)

      if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        personnage.direction = "BAS"
        if personnage.joueur[1]+1 <= len(grille)-1:
          if grille[personnage.joueur[1]+1][personnage.joueur[0]] == 0:
            personnage.déplacement("BAS", grille)

      if keys[pygame.K_LEFT] or keys[pygame.K_a]:
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
    inter.fin_de_jeu()


  compteur = compteur + 1
  if (compteur%4) == 0:
    serpent.recherche_perso(grille)


#MAIN
if __name__ == "__main__":
  Taille_map = 100
  clock = pygame.time.Clock()
  k = 0

  while True:
    carte = Grille(Taille_map)
    grille = carte.generation()
    personnage = perso(Taille_map,grille)
    inter = interface(grille, personnage)
    if k == 0:
      inter.ecran_debut()
      k = k + 1
      serpent =  level_snake().choisir_snake(inter.Niveau.niveau ,grille, personnage, inter)

    run = True
    compteur = 0
    run_game()


