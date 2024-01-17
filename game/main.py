#IMPORT
import pygame
pygame.init()


#CLASS
class interface() :
  def __init__(self, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    self.icon = pygame.image.load("asset\chevalier.png")
    pygame.display.set_icon(self.icon)
    pygame.display.set_caption("Anger Snake")
    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))

  def update_interface_ouvert(self) :
    running = True

    # boucle permettant de rester la fenetre allumé
    while running :

      for event in pygame.event.get() :

        # verifier si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()



class perso() :
    def __init__(self,grille, interface, ):
        self.map = grille
        self.perso = (10,10)
        self.couleur = (0, 255, 0)
        self.interface = interface

    def affiche(self) :
        print(self.interface.surface_dessin, self.couleur, self.perso)
        pygame.draw.rect(self.interface.surface_dessin, self.couleur, self.perso)




#FONCTION




#MAIN
if __name__ == "__main__":
  screen = interface()
  grille = [[0,0,0,0],[0,0,0,1]]
  personnage = perso(grille, screen)


  while True :
    screen.update_interface_ouvert()
    personnage.affiche()
    pygame.display.flip()





