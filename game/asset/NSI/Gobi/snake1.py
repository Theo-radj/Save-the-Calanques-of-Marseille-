import random
from turtle import pos
from hero import *


class Snake1() :
  def __init__(self, map, personnage):
    self.perso = personnage
    self.taille = random.randint(4,8)
    self.position = [(random.randint(self.taille,len(map)-1), random.randint(0,len(map)-1))]
    map[self.position[0][0]][self.position[0][1]]= 3
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
    if map[new_tete[1]][new_tete[0]] == 1:
      self.perso.est_vivant = False
    map[self.position[-1][1]][self.position[-1][0]] = 0
    map[self.position[0][1]][self.position[0][0]] = 3

  def recherche_perso(self,map):

    pos_joueur = self.perso.joueur
    direction = " "
    distance = ((pos_joueur[0]-self.position[0][0] )**2 + (pos_joueur[1]-self.position[0][1])**2)**0.5
    dist_droite = ((pos_joueur[0]-(self.position[0][0]+1) )**2 + (pos_joueur[1]-self.position[0][1])**2)**0.5
    dist_gauche = ((pos_joueur[0]-(self.position[0][0]-1) )**2 + (pos_joueur[1]-self.position[0][1])**2)**0.5
    dist_bas = ((pos_joueur[0]-self.position[0][0] )**2 + (pos_joueur[1]-(self.position[0][1]+1))**2)**0.5
    dist_haut = ((pos_joueur[0]-self.position[0][0] )**2 + (pos_joueur[1]-(self.position[0][1]-1))**2)**0.5

    dist_list = [dist_droite,dist_gauche,dist_bas,dist_haut]
    while direction == " ":
      if len(dist_list) == 0:
        self.revive(map)
      else:
        L= []
        for i in dist_list:
          if distance - i > 0:
            L.append(i)
        if len(L)==0:
          L = dist_list

        dist = L[random.randint(0,len(L)-1)]
        if dist == dist_droite:
          if map[self.position[0][1]][self.position[0][0]+1] == 0 or map[self.position[0][1]][self.position[0][0]+1] == 1 and (self.position[0][0]+1 ,self.position[0][1]) != (self.position[1][0] ,self.position[1][1]):
            direction = "DROITE"
          else:
            dist_list.remove(dist_droite)
        elif dist == dist_gauche:
          if map[self.position[0][1]][self.position[0][0]-1 ] == 0 or map[self.position[0][1]][self.position[0][0]-1 ] == 1 and (self.position[0][0]-1 ,self.position[0][1]) != (self.position[1][0] ,self.position[1][1]):
            direction = "GAUCHE"
          else:
            dist_list.remove(dist_gauche)
        elif dist == dist_bas:
          if map[self.position[0][1]+1][self.position[0][0]] == 0 or map[self.position[0][1]+1][self.position[0][0]] == 1 and (self.position[0][0] ,self.position[0][1]+1) != (self.position[1][0] ,self.position[1][1]):
            direction = "BAS"
          else:
            dist_list.remove(dist_bas)
        elif dist == dist_haut:
          if map[self.position[0][1]-1][self.position[0][0]] == 0 or map[self.position[0][1]-1][self.position[0][0]] == 1 and (self.position[0][0] ,self.position[0][1]-1) != (self.position[1][0] ,self.position[1][1]):
            direction = "HAUT"
          else:
            dist_list.remove(dist_haut)
    self.deplacement(map,direction)

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




