import random
import pygame
from pathfinding import*
from snake import *

class perso() :
  def __init__(self, nb,map):
    self.joueur = [random.randint(0,nb -1 ),random.randint(0,nb - 1)]
    self.couleur = (0, 255, 0)
    map[self.joueur[1]][self.joueur[0]] = 1
    self.direction = "GAUCHE"
    self.pierre_time = 0
    self.old_ticks_time = 0
    self.est_mort = False
    self.score = 0

  def déplacement(self, direction, grille):
    self.direction = direction
    grille[self.joueur[1]][self.joueur[0]] = 0
    if self.direction =="HAUT":
      self.joueur[1] -= 1
    elif self.direction =="BAS":
      self.joueur[1] += 1
    elif self.direction =="GAUCHE":
      self.joueur[0] -= 1
    elif self.direction =="DROITE":
      self.joueur[0] += 1
    grille[self.joueur[1]][self.joueur[0]] = 1

  def casser_pierre(self, grille) :
    time = pygame.time.get_ticks() - self.old_ticks_time
    self.old_ticks_time = pygame.time.get_ticks()
    self.pierre_time += time

    if self.direction =="HAUT" and self.joueur[1]-1 <= len(grille)-1 and grille[self.joueur[1]-1][self.joueur[0]] != 0:
      if self.pierre_time > 200 :
        if grille[self.joueur[1]-1][self.joueur[0]] == 2:
          self.score += 1

          grille[self.joueur[1]-1][self.joueur[0]] -= 2
        else:
          grille[self.joueur[1]-1][self.joueur[0]] -= 4
        self.pierre_time = 0

        if grille[self.joueur[1]-1][self.joueur[0]] < 10:
          grille[self.joueur[1]-1][self.joueur[0]]  = 0

    elif self.direction =="BAS" and self.joueur[1]+1 <= len(grille)-1 and grille[self.joueur[1]+1][self.joueur[0]] != 0:
      if self.pierre_time > 200 :
        if grille[self.joueur[1]+1][self.joueur[0]] == 2:
          self.score += 1

          grille[self.joueur[1]+1][self.joueur[0]] -= 2
        else:
          grille[self.joueur[1]+1][self.joueur[0]] -= 4
        self.pierre_time = 0

        if grille[self.joueur[1]+1][self.joueur[0]] < 10:
          grille[self.joueur[1]+1][self.joueur[0]] = 0

    elif self.direction =="GAUCHE"  and self.joueur[0]-1 <= len(grille[0])-1 and grille[self.joueur[1]][self.joueur[0]-1] != 0:
      if self.pierre_time > 200 :
        if grille[self.joueur[1]][self.joueur[0]-1] == 2:
          self.score += 1

          grille[self.joueur[1]][self.joueur[0]-1] -= 2
        else:
          grille[self.joueur[1]][self.joueur[0]-1] -= 4
        self.pierre_time = 0

        if grille[self.joueur[1]][self.joueur[0]-1] < 10:
          grille[self.joueur[1]][self.joueur[0]-1] = 0

    elif self.direction =="DROITE" and self.joueur[0]+1 <= len(grille[0])-1 and grille[self.joueur[1]][self.joueur[0]+1] != 0 :
      if self.pierre_time > 200 :
        if grille[self.joueur[1]][self.joueur[0+1]] == 2:
          self.score += 1

          grille[self.joueur[1]][self.joueur[0]+1] -= 2
        else:
          grille[self.joueur[1]][self.joueur[0]+1] -= 4
        self.pierre_time = 0

        if grille[self.joueur[1]][self.joueur[0]+1] < 10:
          grille[self.joueur[1]][self.joueur[0]+1] = 0


  def dead(self):

     self.est_mort = True

class Projectile():
    def __init__(self,personnage,direction,grille,serpents):
        self.S = serpents
        self.pos_perso = personnage
        self.dir = direction
        self.sens= ""
        if self.dir == "DROITE":
          self.sens = 4
        elif self.dir == "GAUCHE":
          self.sens = 5
        elif self.dir == "BAS":
          self.sens = 6
        elif self.dir == "HAUT":
          self.sens = 7

        self.pos_proj = [self.pos_perso[0],self.pos_perso[1]]
        if self.dir == "DROITE":
            self.pos_proj[0] += 1
        elif self.dir == "GAUCHE":
            self.pos_proj[0] -= 1
        elif self.dir == "BAS":
            self.pos_proj[1] += 1
        elif self.dir == "HAUT":
            self.pos_proj[1] -= 1
        grille[self.pos_proj[1]][self.pos_proj[0]] =  self.sens


    def movement(self,grille,mort):
        grille[self.pos_proj[1]][self.pos_proj[0]] = 0
        if self.dir == "DROITE":
          if self.pos_proj[0]+1 < len(grille)-1 and grille[self.pos_proj[1]][self.pos_proj[0]+1] <2 :
            self.pos_proj[0] += 1
            case = self.sens
          elif grille[self.pos_proj[1]][self.pos_proj[0]+1] ==3:
            mort = True
            case = 0
            for i in self.S:
              i.hit(self.pos_proj[1],self.pos_proj[0]+1,grille,self.S)
          else:
            mort = True
            case = 0
        elif self.dir == "GAUCHE":
          if self.pos_proj[0] > 0  and grille[self.pos_proj[1]][self.pos_proj[0]-1] <2:
            self.pos_proj[0] -= 1
            case = self.sens
          elif grille[self.pos_proj[1]][self.pos_proj[0]-1] ==3:
            mort = True
            case = 0
            for i in self.S:
              touche = i.hit(self.pos_proj[1],self.pos_proj[0]-1,grille,self.S)
          else:
            mort = True
            case = 0
        elif self.dir == "BAS":
          if self.pos_proj[1]+1 < len(grille)-1 and grille[self.pos_proj[1]+1][self.pos_proj[0]] <2:
            self.pos_proj[1] += 1
            case = self.sens
          elif grille[self.pos_proj[1]+1][self.pos_proj[0]] ==3:
            mort = True
            case = 0
            for i in self.S:
              i.hit(self.pos_proj[1]+1,self.pos_proj[0],grille,self.S)
          else:
            mort = True
            case = 0
        elif self.dir == "HAUT":
          if self.pos_proj[1] > 0 and grille[self.pos_proj[1]-1][self.pos_proj[0]] <2:
            self.pos_proj[1] -= 1
            case = self.sens
          elif grille[self.pos_proj[1]-1][self.pos_proj[0]] ==3:
            mort = True
            case = 0
            for i in self.S:
              i.hit(self.pos_proj[1]-1,self.pos_proj[0],grille,self.S)
          else:
            mort = True
            case = 0

        grille[self.pos_proj[1]][self.pos_proj[0]] = case
        return mort