import random

class perso() :
  def __init__(self, nb,map):
    self.joueur = [random.randint(0,nb -1 ),random.randint(0,nb - 1)]
    self.couleur = (0, 255, 0)
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
    if self.direction =="HAUT" and self.joueur[1]-1 <= len(grille)-1 and grille[self.joueur[0]][self.joueur[1] - 1] != 0:
      grille[self.joueur[0]][self.joueur[1] - 1] -= 3
      if grille[self.joueur[0]][self.joueur[1]-1] < 10:
        grille[self.joueur[0]][self.joueur[1]-1]  = 0
        return True

    elif self.direction =="BAS" and self.joueur[1]+1 <= len(grille)-1 and grille[self.joueur[0]][self.joueur[1] + 1] != 0:
      grille[self.joueur[0]][self.joueur[1] + 1] -= 3
      if grille[self.joueur[0]][self.joueur[1]+1] < 10:
        grille[self.joueur[0]][self.joueur[1]+1] = 0
        return True

    elif self.direction =="GAUCHE"  and self.joueur[0]-1 <= len(grille[0])-1 and grille[self.joueur[0] - 1][self.joueur[1]] != 0:
      grille[self.joueur[0] - 1][self.joueur[1]] -= 3
      if grille[self.joueur[0] - 1][self.joueur[1]] < 10:
        grille[self.joueur[0] - 1][self.joueur[1]] = 0
        return True

    elif self.direction =="DROITE" and self.joueur[0]+1 <= len(grille[0])-1 and grille[self.joueur[0] + 1][self.joueur[1]] != 0 :
      grille[self.joueur[0] + 1][self.joueur[1]] -= 3
      if grille[self.joueur[0] + 1][self.joueur[1]] < 10:
        grille[self.joueur[0] + 1][self.joueur[1]] = 0
        return True


