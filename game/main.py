#IMPORT
import pygame
pygame.init()
import time

#CLASS
class interface() :
  def __init__(self, screen_size=(1080,720)) :
    # générer la fenêtre de notre jeux 
    self.size = screen_size
    self.icon = pygame.image.load("asset\chevalier.png")
    pygame.display.set_icon(self.icon)
    pygame.display.set_caption("Anger Snake")
    self.ecran = pygame.display.set_mode(self.size)


  def update_interface_ouvert(self) :
    running = True

    # boucle permettant de rester la fenetre allumé
    while running :

      for event in pygame.event.get() :
        
        # verifier si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
          running = False
          pygame.quit

  def ecran_acceuil(self) :
    taille_icone_reduit = int(self.size[1]/3)
    self.icon = pygame.transform.scale(self.icon , (taille_icone_reduit,taille_icone_reduit))
    # calcul pour centrer l'icone quelque soit la taille de la fenetre
    r = self.icon.get_rect()
    r.center = self.ecran.get_rect().center


    # appliquer l'icone comme image d'accueil
    self.ecran.blit(self.icon, r)

    # mettre a jour l'ecran
    pygame.display.flip()





#FONCTION




#MAIN
if __name__ == "__main__":
  screen = interface()
  screen.ecran_acceuil()
  screen.update_interface_ouvert()
  




