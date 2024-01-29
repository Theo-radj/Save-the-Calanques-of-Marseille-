import random
import pygame

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
    print(self.grille)

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
    self.grille[self.serpent[-1][0]][self.serpent[-1][0]] = 0
    self.serpent.pop()

    self.interface.ecran.fill((0,0,0))

    self.interface.dessine_serpent(self.serpent, self.couleur)