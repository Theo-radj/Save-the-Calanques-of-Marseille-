#IMPORT
import pygame
pygame.init()


#CLASS
class interface() :
    def __init__(self, screen_size=(1080,720) ) :
      # générer la fenêtre de notre jeux 
      self.nom = pygame.display.set_caption("Anger Snake")
      self.taille = pygame.display.set_mode(screen_size)

    def update_interface(self) :
      running = True

      # boucle permettant de rester la fenetre allumé
      while running :

        for event in pygame.event.get() :
          
          # verifier si le joueur ferme la fenêtre
          if event.type == pygame.QUIT:
            running = False
            pygame.quit
        





#FONCTION




#MAIN
if __name__ == "__main__":
  Screen = interface()
  Screen.update_interface()




