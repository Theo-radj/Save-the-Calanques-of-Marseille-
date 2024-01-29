import random

class perso() :
  def __init__(self, nb,map):

    self.joueur = [random.randint(0,nb),random.randint(0,nb)]
    self.couleur = (0, 255, 0)
    map[self.joueur[0]][self.joueur[1]] = 1

  def déplacement(self,direction,grille):
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
    return grille
