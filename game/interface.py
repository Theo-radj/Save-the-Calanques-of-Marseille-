import pygame
pygame.init()
import sys

class interface() :
  def __init__(self, grille, personnage, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    self.jeu = True
    #self.icon = pygame.image.load("asset\chevalier.png")
    #pygame.display.set_icon(self.icon)
    pygame.display.set_caption("Anger Snake")
    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))
    self.grille = grille
    self.personnage = personnage
    self.taille_tiles = 25
    self.nb_tile_x = self.size[0]//self.taille_tiles
    self.nb_tile_y = self.size[1]//self.taille_tiles
    self.centre_x = int((self.nb_tile_x)//2)
    self.centre_y = int((self.nb_tile_y)//2)
    self.max_horizontal_centre = len(self.grille) - self.centre_x
    self.max_vertical_centre = len(self.grille[0]) - self.centre_y

  def update_interface_ouvert(self) :
    # boucle permettant de rester la fenetre allumé
      for event in pygame.event.get() :
        # verifier si le joueur ferme la fenêtre

        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] :
          pygame.quit()
          sys.exit()
          return False
          
      return True

  def analyse_grille(self):
    #cette fonction a chaque itération permet  d'analyser les cases de la grille
    #et d'appeler les bonnes fonctions pour afficher ce qu'il y a à ces endroits
    self.ecran.fill((0,0,0))
    for i in range(len(self.grille)):
      for j in range(len(self.grille[i])):
        x,y = self.camera_perso(i, j)
        affiche = self.grille[i][j]

        if affiche <= 20 and affiche >= 10 :
          self.dessine_rocher(x,y, affiche)

        elif affiche == 1:
          self.dessine_perso(x,y)

        elif affiche == 3:
            self.dessine_serpent(x,y)
    pygame.display.flip()

  def camera_perso(self, x, y) :
    #cette fontion permet de savoir si on centre le joueur au milieu
    #de l'ecran ou pas  et ainsi cela permettrai au joueur d'etre
    #en haut a droite s'il est au bout de la map au lieu du milieu
    if self.personnage.joueur[0] < self.centre_x :
      self.camera_x = x
    elif  self.personnage.joueur[0] > self.max_horizontal_centre :
      self.camera_x = self.centre_x + x - self.max_horizontal_centre
    else:
      self.camera_x = x - self.personnage.joueur[0] + self.centre_x

    if self.personnage.joueur[1] < self.centre_y :
      self.camera_y = y
    elif  self.personnage.joueur[1] > self.max_vertical_centre :
      self.camera_y = self.centre_y + y - self.max_vertical_centre
    else:
      self.camera_y = y - self.personnage.joueur[1] + self.centre_y

    return self.camera_x, self.camera_y

  def deplace_camera(self, vitesse) :
    self.centre_x += vitesse[0]
    self.centre_y += vitesse[1]

  def dessine_serpent(self, x,y):
    pygame.draw.rect(self.ecran, ((255,255,0)), (x*self.taille_tiles, y*self.taille_tiles,self.taille_tiles,self.taille_tiles))

  def dessine_rocher(self, x,y, taux):
    couleur = int(255*taux/20)
    pygame.draw.rect(self.ecran, (couleur,couleur,couleur), (x*self.taille_tiles, y*self.taille_tiles,self.taille_tiles,self.taille_tiles))

  def dessine_perso(self,x,y):
    pygame.draw.rect(self.ecran, ((0,255,0)), (x*self.taille_tiles, y*self.taille_tiles,self.taille_tiles,self.taille_tiles))

  def fin_de_jeu(self):
    while not pygame.key.get_pressed() :
      self.dessine_rocher(10,10,20)
    self.jeu = False