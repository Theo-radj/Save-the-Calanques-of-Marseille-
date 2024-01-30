import random

class perso() :
  def __init__(self, nb,map):
    self.joueur = [random.randint(0,nb -1 ),random.randint(0,nb - 1)]
    self.couleur = (0, 255, 0)
    print(self.joueur)
    map[self.joueur[0]][self.joueur[1]] = 1
    self.direction = " "

  def déplacement(self, direction, grille):
    self.direction = direction
    grille[self.joueur[0]][self.joueur[1]] = 0
    if self.direction =="HAUT":
      self.joueur[1] -= 1
    elif self.direction =="BAS":
      self.joueur[1] += 1
    elif self.direction =="GAUCHE":
      self.joueur[0] -= 1
    elif self.direction =="DROITE":
      self.joueur[0] += 1
    grille[self.joueur[0]][self.joueur[1]] = 1

  def casser_pierre(self, grille) :
    if self.direction =="HAUT":
      grille[self.joueur[0]][self.joueur[1] - 1] = 0
    elif self.direction =="BAS":
      grille[self.joueur[0]][self.joueur[1] + 1] = 0
    elif self.direction =="GAUCHE":
      grille[self.joueur[0] - 1][self.joueur[1]] = 0
    elif self.direction =="DROITE":
      grille[self.joueur[0] + 1][self.joueur[1]] = 0



