#IMPORT
from hero import *
from interface import *
from snake import *
from map import *


#FONCTION
def run_game() :
  while inter.jeu :
    inter.interface_ferme()
    inter.analyse_grille(nombre_de_sacs)
    control()
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
  global game_time
  if personnage.score == nombre_de_sacs:
    score(game_time)
    inter.mission_completed()

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
    game_time += time

    if keys:
      if (compteur%2) == 0:
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
  if (compteur%vitesse_serpent) == 0:
    for serpent in serpents:
      serpent.recherche_perso(grille)
    if len(serpents) == 0:
      serpents.append(Snake(grille,personnage))


def score(game_time) :
  with open ("asset/score.txt", 'r') as fichier :
    Liste_score = [0]*20
    k = 0
    for i in fichier.readlines():
      Liste_score[k] = int(i)
      k = k + 1
  personnage.score = int((personnage.score/(game_time/1000))*1000)
  for i in range(5):
    if personnage.score >= Liste_score[i] :
        list_tempo = Liste_score[i:]
        for j in range(len(list_tempo) - 1, 0, -1):
          Liste_score[i+j] = list_tempo[j-1]
        Liste_score[i] = personnage.score
        break

  with open ("asset/score.txt", 'w') as fichier :
    for i in Liste_score[:5] :
      fichier.write(f"{i}\n")



#MAIN
if __name__ == "__main__":
  Taille_map = 100
  clock = pygame.time.Clock()
  k = 0
  vitesse_serpent = 0
  while True:
    carte = Grille(Taille_map)
    grille,nombre_de_sacs = carte.generation()
    personnage = perso(Taille_map,grille)
    inter = interface(grille, personnage)
    serpents = []
    run = True
    projectiles = []

    compteur = 0
    game_time = 0
    epine_time = 0
    old_ticks_time = 0

    serpents.append(Snake(grille, personnage))
    if k == 0:
      inter.ecran_debut()
      k = k + 1
    if inter.Niveau.niveau == 1:
      vitesse_serpent = 7
    elif inter.Niveau.niveau == 2:
      vitesse_serpent = 5
    elif inter.Niveau.niveau == 3:
      vitesse_serpent = 4
      serpents.append(Snake(grille, personnage))
    serpents.append(Snake(grille, personnage))

    run_game()






