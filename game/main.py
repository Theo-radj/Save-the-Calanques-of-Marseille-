#IMPORT
import pygame
pygame.init()

import sys
import random




nb_x = 45
nb_y = 45


pos_joueur = [random.randint(0,nb_x),random.randint(0,nb_y)]


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

          pygame.quit()
          return False
          sys.exit
      return True

  def analyse_grille(self):
    global grille
    #self.ecran.fill((0,0,0))
    for i in range(len(grille)):
      for j in range(len(grille[i])):
        if grille[i][j] == 2 :
          self.dessine_rocher(i,j)
        elif grille[i][j] == 1 :
          self.dessine_perso(i,j)



  def dessine_serpent(self, serpent, couleur):
    for i in serpent :
      pygame.draw.rect(self.ecran, couleur, (i[0], i[1],64,64))
    pygame.display.flip()

  def dessine_rocher(self, x,y):
    pygame.draw.rect(self.ecran, ((255,255,255)), (x*16, y*16,16,16))
    pygame.display.flip()

  def dessine_perso(self,x,y):
    pygame.draw.rect(self.ecran, ((0,255,0)), (x*16, y*16,16,16))
    pygame.display.flip()


class perso() :
  def __init__(self, joueur):
    self.joueur = joueur
    self.couleur = (0, 255, 0)
    grille[self.joueur[0]][self.joueur[1]] = 1

  def déplacement(self,direction):
    global grille
    grille[self.joueur[0]][self.joueur[1]] = 0
    if direction =="HAUT":
      self.joueur[1] -= 1
    elif direction =="BAS":
      self.joueur[1] += 1
    elif direction =="GAUCHE":
      self.joueur[0] -= 1
    elif direction =="DROITE":
      self.joueur[0] += 1
    grille[self.joueur[0]][self.joueur[1]] = 1

class ennemi() :
  def __init__(self, couleur, interface, grille):
    self.couleur = couleur
    self.interface = interface
    self.taille = random.randint(2,5)
    self.grille = grille

    k,j = random.randint(3,72), random.randint(0,72)
    self.serpent = [(k*10 , j*10), (k*10-10, j*10), (k*10-20, j*10)]


  def Serpent(self) :
    #global direction , grille
    for i in self.serpent :
      print(i)
      self.grille[i[0]][i[1]] = 1
    print(grille)

    tete = list(self.serpent[0])

    if direction == "HAUT":
      tete[1] -= 10
    elif direction == "BAS":
      tete[1] += 10
    elif direction == "GAUCHE":
      tete[0] -= 10
    elif direction == "DROITE":
      tete[0] += 10


    if tete[0] < 0 or tete[1] < 0 :
      pygame.quit()

    self.serpent.insert(0, tete)
    grille[self.serpent[-1][0]][self.serpent[-1][0]] = 0
    self.serpent.pop()

    self.interface.ecran.fill((0,0,0))

    self.interface.dessine_serpent(self.serpent, self.couleur)



#FONCTION
def control():
  global direction
  keys = pygame.key.get_pressed()
  if keys:
    if keys[pygame.K_UP]:
      personnage.déplacement("HAUT")


    elif keys[pygame.K_DOWN]:
      personnage.déplacement("BAS")


    elif keys[pygame.K_LEFT]:
      personnage.déplacement("GAUCHE")


    elif keys[pygame.K_RIGHT]:
      personnage.déplacement("DROITE")


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
  personnage = perso(pos_joueur)

  clock = pygame.time.Clock()

  run = True

  while run :
    run = inter.update_interface_ouvert()
    control()
    inter.analyse_grille()
    clock.tick(30)

