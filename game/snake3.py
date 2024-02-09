import random
from hero import *
from pathfinding import *

class Snake3() :
  def __init__(self, map, personnage):
    self.perso = personnage
    self.taille = random.randint(4,8)
    self.position = [(random.randint(self.taille,len(map)-1), random.randint(0,len(map)-1))]
    map[self.position[0][1]][self.position[0][0]]= 3
    for i in range(1,self.taille):
        self.position.append(((self.position[0][0]-i),(self.position[0][1])))



  def deplacement(self, map, direction) :
    tete = self.position[0]
    if direction == "HAUT":
      new_tete = (tete[0]),(tete[1]-1)
    elif direction == "BAS":
      new_tete = (tete[0]),(tete[1]+1)
    elif direction == "GAUCHE":
      new_tete = (tete[0]-1),(tete[1])
    elif direction == "DROITE":
      new_tete = (tete[0]+1),(tete[1])
    else:
      new_tete = tete

    self.position.insert(0, new_tete)
    self.position.pop()
    map[self.position[-1][1]][self.position[-1][0]] = 0
    map[self.position[0][1]][self.position[0][0]] = 3


  def recherche_perso(self, map, perso ):
    pos_joueur = perso.joueur[0] , perso.joueur[1]
    coo_serpent = self.position[0]
    path = find_path(map,coo_serpent,pos_joueur)
    direction = ""
    if path != False:
      if len(path)==1:
        perso.est_vivant = False
      else:
        if path[1][1] == coo_serpent[1] + 1:
          direction = "BAS"
        elif path[1][1] == coo_serpent[1] - 1:
          direction = "HAUT"
        elif path[1][0] == coo_serpent[0] + 1:
          direction = "DROITE"
        elif path[1][0] == coo_serpent[0] - 1:
          direction = "GAUCHE"
      self.deplacement(map,direction)
    else:
      self.revive(map)

  def revive(self,map):
    map[self.position[0][1]][self.position[0][0]]= 0
    self.position = [(random.randint(self.taille,45), random.randint(0,45))]
    map[self.position[0][1]][self.position[0][0]]= 3
    for i in range(1,self.taille):
        self.position.append(((self.position[0][0]-i),(self.position[0][1])))






