#import
import pygame


#class






#fonction




#main
pygame.init()
pygame.display.set_caption("Anger Snake")
pygame.display.set_mode((960,540))

running = True

while running :
  #screen.blit(background,(0.0))
  pygame.disflip.flip()

  for event in pygame.event.get() :
    if event.type == pygame.QUIT:
      running = False
      pygame.quit



