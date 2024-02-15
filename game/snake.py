import random
from hero import*
from pathfinding import*


class Snake() :
  def __init__(self, map,personnage):
    self.perso = personnage
    self.taille = random.randint(4,8)
    self.position = [(random.randint(self.taille,len(map)-1), random.randint(0,len(map)-1))]
    map[self.position[0][1]][self.position[0][0]]= 3
    for i in range(1,self.taille):
        self.position.append(((self.position[0][0]-i),(self.position[0][1])))
    self.direction = ""
  def deplacement(self,map) :

    tete = self.position[0]
    if self.direction == "HAUT":
      new_tete = (tete[0]),(tete[1]-1)
    elif self.direction == "BAS":
      new_tete = (tete[0]),(tete[1]+1)
    elif self.direction == "GAUCHE":
      new_tete = (tete[0]-1),(tete[1])
    elif self.direction == "DROITE":
      new_tete = (tete[0]+1),(tete[1])
    else:
      new_tete = tete

    self.position.insert(0, new_tete)
    self.position.pop()
    map[self.position[-1][1]][self.position[-1][0]] = 0
    map[self.position[0][1]][self.position[0][0]] = 3

  def recherche_perso(self,map):
    pos_joueur = self.perso.joueur[0],self.perso.joueur[1]
    coo_serpent = self.position[0]
    path = find_path(map,coo_serpent,pos_joueur)
    if path != False:
      if len(path)==1:
        self.perso.dead()
      else:
        if path[1][1] == coo_serpent[1] + 1:
          self.direction = "BAS"
        elif path[1][1] == coo_serpent[1] - 1:
          self.direction = "HAUT"
        elif path[1][0] == coo_serpent[0] + 1:
          self.direction  = "DROITE"
        elif path[1][0] == coo_serpent[0] - 1:
          self.direction = "GAUCHE"
      self.deplacement(map)
    else:
      self.revive(map)

  def hit(self,y,x,map,S):
    touche = False
    for i in self.position:
      if i == (x,y):
        touche = True

    if touche == True:

      if len(self.position)> 4:
        for i in range(2):
          self.position.pop()
          map[self.position[-1][1]][self.position[-1][0]] = 0
      else:
        for i in range(len(self.position)):
          map[self.position[i][1]][self.position[i][0]] = 0
        S.remove(self)




  def revive(self,map):
    for i in range(len(self.position)):
          map[self.position[i][1]][self.position[i][0]] = 0
    map[self.position[0][1]][self.position[0][0]]= 0
    self.position = [(random.randint(self.taille,45), random.randint(0,45))]
    map[self.position[0][1]][self.position[0][0]]= 3
    for i in range(1,self.taille):
        self.position.append(((self.position[0][0]-i),(self.position[0][1])))







