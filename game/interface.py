import pygame
pygame.init()
import sys


class interface() :
  def __init__(self, grille, personnage, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    self.jeu = True
    pygame.display.set_caption("Anger Snake")

    self.icon = pygame.image.load("asset/chevalier.png")
    pygame.display.set_icon(self.icon)

    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))
    self.grille = grille
    self.personnage = personnage
    self.taille_tiles = 36
    self.nb_tile_x = self.size[0]//self.taille_tiles
    self.nb_tile_y = self.size[1]//self.taille_tiles
    self.centre_x = int((self.nb_tile_x)//2)
    self.centre_y = int((self.nb_tile_y)//2)
    self.max_vertical_centre = len(self.grille) - self.centre_y
    self.max_horizontal_centre = len(self.grille[0]) - self.centre_x

    self.fond= pygame.image.load("asset/0000.png")
    self.tiles_size_fond = 256
    self.fond = pygame.transform.scale(self.fond, (self.tiles_size_fond, self.tiles_size_fond))

    self.rock= pygame.image.load("asset/rocks0.png")
    self.rock = pygame.transform.scale(self.rock, (self.taille_tiles,self.taille_tiles))

    self.rock2 = pygame.image.load("asset/rocks1.png")
    self.rock2 = pygame.transform.scale(self.rock2, (self.taille_tiles,self.taille_tiles))

    self.perso_sprite = pygame.image.load("asset/poissin3.png")
    self.perso_sprite = pygame.transform.scale(self.perso_sprite, (self.taille_tiles,self.taille_tiles))

    self.poubelle = pygame.image.load("asset/sac_poubelle.png")
    self.poubelle = pygame.transform.scale(self.poubelle, (self.taille_tiles,self.taille_tiles))

    self.exit_button = pygame.image.load("asset/exit_button.png")
    self.play_button = pygame.image.load("asset/play_button.png")

    self.police = pygame.font.Font("asset/ARCADECLASSIC.ttf",64)
    self.score = 0
    #self.click_sound = pygame.mixer.Sound("asset/click_sound.mp3")
    #self.bruit_dead = pygame.mixer.Sound("asset/dead.mp3")
    #self.bruit_rocher = pygame.mixer.Sound("asset/casser_pierre.mp3")
    self.Niveau = Niveau(self)


  def interface_ferme(self) :
      for event in pygame.event.get() :
        if event.type == pygame.QUIT :
          pygame.quit()
          sys.exit()
          return False
      return True

  def analyse_grille(self):
    #cette fonction a chaque itération permet  d'analyser les cases de la grille
    #et d'appeler les bonnes fonctions pour afficher ce qu'il y a à ces endroits
    self.ecran.fill((0,0,0))
    for v in range(0,self.size[0],self.tiles_size_fond):
            for b in range(0,self.size[1],self.tiles_size_fond):
                self.ecran.blit( self.fond,(v,b))
    for i in range(len(self.grille)):
      for j in range(len(self.grille[i])):
        x,y = self.camera_perso(j, i)
        affiche = self.grille[i][j]

        if affiche <= 20 and affiche >= 10 :
          self.dessine_rocher(x,y, j,i)

        elif affiche == 1:
          self.dessine_perso(x,y)

        elif affiche == 3:
            self.dessine_serpent(x,y)

        elif affiche == 4 :
            self.dessine_sac_poubelle(x,y)
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

  def dessine_rocher(self, x,y, X,Y):
    if Y<len(self.grille)-1:
      if self.grille[Y+1][X]>3:
        self.ecran.blit( self.rock2,(x*self.taille_tiles,y*self.taille_tiles))
      else:
        self.ecran.blit(self.rock,(x*self.taille_tiles,y*self.taille_tiles))
    else:
      self.ecran.blit(self.rock2,(x*self.taille_tiles,y*self.taille_tiles))

  def dessine_sac_poubelle(self, x,y):
    self.ecran.blit(self.poubelle,(x*self.taille_tiles,y*self.taille_tiles))

  def dessine_perso(self,x,y):
    self.ecran.blit( self.perso_sprite,(x*self.taille_tiles,y*self.taille_tiles))

  def fin_de_jeu(self):
    self.ecran.fill((0,0,0))
    texte1 = self.police.render("Game Over ! ", True , (255,255,255))
    self.ecran.blit(texte1,(texte1.get_rect(center = (self.size[0]//2, 150 ))))

    texte2 = self.police.render("Score   "+ str(self.score),True , (255,255,255))
    self.ecran.blit(texte2,(texte2.get_rect(center = (self.size[0]//2, 200 ))))
    self.ecran_tempo()

  def ecran_debut(self):
    self.ecran.fill((0,0,0))

    texte1 = self.police.render("Bienvenue", True , (255,255,255))
    self.ecran.blit(texte1,(texte1.get_rect(center = (self.size[0]//2, 150 ))))

    texte2 = self.police.render("dans  notre  jeux",True , (255,255,255))
    self.ecran.blit(texte2,(texte2.get_rect(center = (self.size[0]//2, 200 ))))
    self.ecran_tempo()

  def ecran_pause(self):
    pause = True
    while pause:
      texte = self.police.render("Pause", True , (255,255,255))
      position = (self.size[0]//2, 150 )
      texte_rect = texte.get_rect(center = position)
      pygame.draw.rect(self.ecran, (10,10,10), texte_rect, 100)
      self.ecran.blit(texte,texte_rect)
      pause = self.ecran_tempo()
      self.jeu = True

  def ecran_tempo(self):
    play = pygame.transform.scale(self.play_button.convert_alpha(), (200,200))
    exit = pygame.transform.scale(self.exit_button.convert_alpha(), (200,100))

    play_button_rect = play.get_rect(center = (self.size[0]//2, 300))
    exit_button_react = exit.get_rect(center = (self.size[0]//2, 500 ))
    self.ecran.blit(play,play_button_rect)
    self.ecran.blit(exit,exit_button_react)
    pygame.display.flip()

    ecran_tempo = True
    while ecran_tempo :
      self.interface_ferme()
      pygame.time.Clock().tick(30)
      mouse_x, mouse_y = pygame.mouse.get_pos()

      if play_button_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[pygame.K_SPACE]:
        pygame.time.delay(100)
        if pygame.mouse.get_pressed()[0]:
          pass
          #self.click_sound.play()
        self.Niveau.niveau_montrer()
        self.jeu = False
        ecran_tempo = False
        return False

      elif exit_button_react.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
        pygame.quit()
        sys.exit()


class Niveau():
  def __init__(self, inter):
    self.inter = inter
    self.niveau = 0

  def niveau_montrer(self):
    self.inter.ecran.fill((0,0,0))
    
    if self.niveau == 0 :
      niveau1 = self.inter.police.render("Niveau 1",True , (255,255,255))
      niveau1_rect = niveau1.get_rect(center = (self.inter.size[0]//2, 300))
      self.inter.ecran.blit(niveau1,niveau1_rect)

      niveau2 = self.inter.police.render("Niveau 2",True , (255,255,255))
      niveau2_rect = niveau2.get_rect(center = (self.inter.size[0]//2, 400 ))
      self.inter.ecran.blit(niveau2,niveau2_rect)
      
      niveau3 = self.inter.police.render("Niveau 3",True , (255,255,255))
      niveau3_rect = niveau3.get_rect(center = (self.inter.size[0]//2, 500 ))
      self.inter.ecran.blit(niveau3, niveau3_rect)
      pygame.display.flip()

      while pygame.mouse.get_pressed()[0]:
        print(pygame.mouse.get_pressed())
        for  event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONUP :
            pass
        pygame.time.wait(100)
           

      while self.niveau == 0 :
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if niveau1_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] :
          self.niveau = 1

        if niveau2_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] :
          self.niveau  = 2  

        if niveau3_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] :
          self.niveau = 3
        self.inter.interface_ferme()

