import pygame
class interface() :
  def __init__(self, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    pygame.display.set_caption("Anger Snake")
    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))
    self.tiles = 16


  def update_interface_ouvert(self) :
    # boucle permettant de rester la fenetre allumé
      for event in pygame.event.get() :
        # verifier si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:

          pygame.quit()
          return False
          sys.exit
      return True

  def analyse_grille(self,grille):
    self.ecran.fill((0,0,0))
    for i in range(len(grille)):
      for j in range(len(grille[i])):
        if grille[i][j] == 2 :
          self.dessine_rocher(i,j)
        elif grille[i][j] == 1:
            self.dessine_perso(i,j)
        elif grille[i][j] == 3:
            self.dessine_serpent(i,j)
    pygame.display.flip()




  def dessine_serpent(self, x,y):
    pygame.draw.rect(self.ecran, ((255,255,0)), (x*self.tiles, y*self.tiles,self.tiles,self.tiles))


  def dessine_rocher(self, x,y):
    pygame.draw.rect(self.ecran, ((255,255,255)), (x*self.tiles, y*self.tiles,self.tiles,self.tiles))


  def dessine_perso(self,x,y):
    pygame.draw.rect(self.ecran, ((0,255,0)), (x*self.tiles, y*self.tiles,self.tiles,self.tiles))
