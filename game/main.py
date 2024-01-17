#IMPORT
import pygame
pygame.init()

import sys
import random



nb_x = 500
nb_y = 500

grille =  [[0 for y in range(nb_x)] for x in range(nb_y)]
pos_joueur = (random.randint(0,nb_x),random.randint(0,nb_y))
grille[pos_joueur[0]-1][pos_joueur[1]-10] = 1

direction = "DROITE"
#CLASS
class interface() :
  def __init__(self, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    self.icon = pygame.image.load("asset\chevalier.png")
    pygame.display.set_icon(self.icon)
    pygame.display.set_caption("Anger Snake")
    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))

  def update_interface_ouvert(self) :
    # boucle permettant de rester la fenetre allumé
      for event in pygame.event.get() :
        # verifier si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
          return False
          pygame.quit()
          sys.exit
      return True
          
  def dessine_serpent(self, serpent, couleur):
    for i in serpent :
      pygame.draw.rect(self.ecran, couleur, (200, 200,10,10))
      pygame.display.flip()


class perso() :
  def __init__(self, joueur, interface):
    self.joueur = joueur
    self.perso = (10,10)
    self.couleur = (0, 255, 0)
    self.interface = interface


class ennemi() :
  def __init__(self, couleur, interface):
    self.couleur = couleur
    self.interface = interface
    self.taille = random.randint(2,5)
    self.serpent = [(3, 1), (2, 1), (1, 1)]
     

  def Serpent(self, direction) :
    for i in self.serpent :
      grille[i[0]][i[1]] = 1

    tete = list(self.serpent[0])

    if direction == "HAUT":
      tete[1] -= 10
    if direction == "BAS":
      tete[1] += 10
    if direction == "GAUCHE":
      tete[0] -= 10
    if direction == "DROITE":
      tete[0] += 10

    self.serpent.insert(0, tete)
    self.serpent.pop()

    self.interface.ecran.fill((0,0,0))

    for i in self.serpent :
      pygame.draw.rect(self.interface.ecran, self.couleur, (i[0], i[1],10,10))
    pygame.display.flip()
    



#FONCTION
def control(direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not direction == "BAS":
      direction = "HAUT"

    elif keys[pygame.K_DOWN] and not direction == "HAUT":
      direction = "BAS"

    elif keys[pygame.K_LEFT] and not direction == "DROITE":
      direction = "GAUCHE"

    elif keys[pygame.K_RIGHT] and not direction == "GAUCHE":
      direction = "DROITE"

    mechant1.Serpent(direction)


#MAIN
if __name__ == "__main__":
  
  inter = interface()
  mechant1 = ennemi((0,255,0),inter)
  personnage = perso(pos_joueur, inter)

  clock = pygame.time.Clock()

  run = True

  while run :
    run = inter.update_interface_ouvert()
    direction = control(direction)

    clock.tick(30)

