import random

class Grille():
    def __init__(self,taille):
        self.taille_map = taille
        self.my_map = [[0 for _ in range(self.taille_map)] for _ in range(self.taille_map)]

    def generation(self):
        for x in range (3):
            for i in range(self.taille_map):
                for j in range(self.taille_map):
                    if self.my_map[(i+1)%self.taille_map][(j+1)%self.taille_map] == 20 or self.my_map[(i+1)%self.taille_map][j] == 20 or self.my_map[i][(j+1)%self.taille_map] == 20 or self.my_map[(i-1)%self.taille_map][j] == 20 or self.my_map[(i-1)%self.taille_map][(j-1)%self.taille_map] or self.my_map[i][(j-1)%self.taille_map] == 20:
                        chance = 580
                    else:
                        chance = 998
                    if random.randint(0,1000) > chance:
                        self.my_map[i][j] = 20
        self.poser_poubelle()
        return self.my_map



    def poser_poubelle(self):
      chance = 92
      for i in range(len(self.my_map)):
        for j in range(len(self.my_map[1])) :
          if self.my_map[(i+1)%self.taille_map][(j+1)%self.taille_map] == 20 and self.my_map[(i+1)%self.taille_map][j] == 20 and self.my_map[(i+1)%self.taille_map][(j-1)%self.taille_map] == 20 and self.my_map[i][(j+1)%self.taille_map] == 20 and self.my_map[(i-1)%self.taille_map][(j)%self.taille_map] == 20 and self.my_map[(i-1)%self.taille_map][(j-1)%self.taille_map] == 20 and self.my_map[(i-1)%self.taille_map][(j+1)%self.taille_map] == 20 :
            if random.randint(0,100) > chance :
                self.my_map[i][j] = 4




