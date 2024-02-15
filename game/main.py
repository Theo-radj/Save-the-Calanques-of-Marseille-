#IMPORT
from hero import *
from interface import *
import snake
from map import*
import snake1
#FONCTION

def run_game() :
  while inter.jeu :
    control()
    inter.interface_ferme()
    inter.analyse_grille()
    clock.tick(30)


def control():
  global personnage
  global grille
  global inter
  global compteur
  global projectiles
  global old_ticks_time
  global epine_time
  global serpents

  keys = pygame.key.get_pressed()
  if personnage.est_mort == False:
    for projectile in projectiles:
      detruit = False
      detruit = projectile.movement(grille,detruit)
      if detruit == True:
        projectiles.remove(projectile)


    time = pygame.time.get_ticks() - old_ticks_time
    old_ticks_time = pygame.time.get_ticks()
    epine_time += time


    if keys:
      if (compteur%2) == 0:
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
        if personnage.direction == "DROITE" and personnage.joueur[0]<len(grille)-1:
            if grille[personnage.joueur[1]][personnage.joueur[0]+1] > 10 or grille[personnage.joueur[1]][personnage.joueur[0]+1] == 2 :
                personnage.casser_pierre(grille)
                epine_time = 0
            else:
              if grille[personnage.joueur[1]][personnage.joueur[0]+1] == 0 and epine_time > 1000:
                proj = Projectile(personnage.joueur,personnage.direction,grille,serpents)
                projectiles.append(proj)
                epine_time = 0

        elif personnage.direction == "GAUCHE" and personnage.joueur[0]>0:
            if grille[personnage.joueur[1]][personnage.joueur[0]-1] > 10 or grille[personnage.joueur[1]][personnage.joueur[0]-1] == 2:
                personnage.casser_pierre(grille)
                epine_time = 0
            else:
              if grille[personnage.joueur[1]][personnage.joueur[0]-1] == 0 and epine_time > 1000:
                proj = Projectile(personnage.joueur,personnage.direction,grille,serpents)
                projectiles.append(proj)
                epine_time = 0
        elif personnage.direction == "HAUT" and personnage.joueur[1]>0:
            if grille[personnage.joueur[1]-1][personnage.joueur[0]] > 10 or grille[personnage.joueur[1]-1][personnage.joueur[0]] == 2:
                personnage.casser_pierre(grille)
                epine_time = 0
            else:
              if grille[personnage.joueur[1]-1][personnage.joueur[0]] == 0  and epine_time > 1000:
                proj = Projectile(personnage.joueur,personnage.direction,grille,serpents)
                projectiles.append(proj)
                epine_time = 0
        elif personnage.direction == "BAS" and personnage.joueur[1]<len(grille)-1:
            if grille[personnage.joueur[1]+1][personnage.joueur[0]] > 10 or grille[personnage.joueur[1]+1][personnage.joueur[0]] == 2:
                personnage.casser_pierre(grille)
                epine_time = 0

            else:
              if grille[personnage.joueur[1]+1][personnage.joueur[0]] == 0  and epine_time > 1000:
                proj = Projectile(personnage.joueur,personnage.direction,grille,serpents)
                projectiles.append(proj)
                epine_time = 0


  else:
    inter.fin_de_jeu()


  compteur = compteur + 1
  if (compteur%6) == 0:
    for serpent in serpents:
      serpent.recherche_perso(grille)
    if len(serpents) == 0:
      serpents.append(Snake(grille,personnage))




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
    serpents = []
    run = True
    projectiles = []

    compteur = 0

    epine_time = 0
    old_ticks_time = 0
    if k == 0:
      inter.ecran_debut()
      k = k + 1
      if inter.Niveau.niveau == 1:
        serpents.append(snake1.Snake1(grille, personnage))
      elif inter.Niveau.niveau == 2:
        serpents.append(snake.Snake(grille, personnage))

    run_game()



