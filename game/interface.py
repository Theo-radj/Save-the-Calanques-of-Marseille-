import pygame


class interface() :
  def __init__(self, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    self.icon = pygame.image.load("asset\chevalier.png")
    pygame.display.set_icon(self.icon)
    pygame.display.set_caption("Anger Snake")
    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))
    self.tiles = 16
    self.nb_tile_x = self.size[0]//self.tiles
    self.nb_tile_y = self.size[1]//self.tiles
    self.centre_x = int((self.nb_tile_x)//2)
    self.centre_y = int((self.nb_tile_y)//2)
    self.max_horizontal_centre = 0
    self.max_vertical_centre = 0


  def update_interface_ouvert(self) :
    # boucle permettant de rester la fenetre allumé
      for event in pygame.event.get() :
        # verifier si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:

          pygame.quit()
          return False
          sys.exit()
      return True

  def analyse_grille(self, grille, personnage):
    self.ecran.fill((0,0,0))
    for i in range(len(grille)):
      for j in range(len(grille[i])):
        x,y = self.camera_perso(personnage, grille, i, j)
        if grille[i][j] == 2 :
          self.dessine_rocher(x,y)
        elif grille[i][j] == 1:
          
          self.dessine_perso(x,y)
    pygame.display.flip()

  def camera_perso(self, personnage, grille, x, y) :
    max_horizontal_centre = len(grille) - self.centre_x
    max_vertical_centre = len(grille[0]) - self.centre_y

    if personnage.joueur[0] < self.centre_x :
      self.camera_x = x
    elif  personnage.joueur[0] > max_horizontal_centre :
      self.camera_x = self.centre_x + x - max_horizontal_centre
    else:
      self.camera_x = x - personnage.joueur[0] + self.centre_x

    if personnage.joueur[1] < self.centre_y :
      self.camera_y = y
    elif  personnage.joueur[1] > max_vertical_centre :
      self.camera_y = self.centre_y + y - max_vertical_centre 
    else:
      self.camera_y = y - personnage.joueur[1] + self.centre_y





    return self.camera_x, self.camera_y

  def deplace_camera(self, vitesse) :
    self.centre_x += vitesse[0]
    self.centre_y += vitesse[1]


  def dessine_serpent(self, serpent, couleur):
    for i in serpent :
      pygame.draw.rect(self.ecran, couleur, (i[0], i[1],self.tiles,self.tiles))
    pygame.display.flip()

  def dessine_rocher(self, x,y):
    pygame.draw.rect(self.ecran, ((255,255,255)), (x*self.tiles, y*self.tiles,self.tiles,self.tiles))


  def dessine_perso(self,x,y):
    pygame.draw.rect(self.ecran, ((0,255,0)), (x*self.tiles, y*self.tiles,self.tiles,self.tiles))
