import pygame
pygame.init()
import sys
import random



class interface() :
  def __init__(self, grille, personnage, screen_size=(720,720)) :
    # générer la fenêtre de notre jeux
    self.size = screen_size
    self.jeu = True
    pygame.display.set_caption("Anger Snake")

    self.icon = pygame.image.load("asset/logo.jpeg")
    pygame.display.set_icon(self.icon)

    self.tiles_size_fond = 256
    self.fond = []
    for i in range (0,40):
      if i < 10:
        i = "0"+str(i)
      else:
        i = str(i)
      self.fond.append(pygame.transform.scale((pygame.image.load('asset/water_128px_frames/00'+i+".png")), (self.tiles_size_fond, self.tiles_size_fond)))
    self.index = 0

    self.taille_tiles = 36
    self.rock= pygame.image.load("asset/rocks0.png")
    self.rock = pygame.transform.scale(self.rock, (self.taille_tiles,self.taille_tiles))

    self.rock2 = pygame.image.load("asset/rocks1.png")
    self.rock2 = pygame.transform.scale(self.rock2, (self.taille_tiles,self.taille_tiles))

    self.epine = pygame.image.load("asset/epine.png")
    self.epine = pygame.transform.scale(self.epine, (self.taille_tiles,self.taille_tiles))

    self.perso_d = pygame.image.load("asset/poissin3.png")
    self.perso_d = pygame.transform.scale(self.perso_d, (self.taille_tiles,self.taille_tiles))

    self.exit_button = pygame.image.load("asset/exit_button.png")
    self.play_button = pygame.image.load("asset/play_button.png")

    self.poubelle = pygame.image.load("asset/sac_poubelle.png")
    self.poubelle = pygame.transform.scale(self.poubelle, (self.taille_tiles,self.taille_tiles))

    self.police = pygame.font.Font("asset/ARCADECLASSIC.ttf",64)

    self.tete = pygame.image.load("asset/murene/murene0.png")
    self.tete = pygame.transform.scale(self.tete, (self.taille_tiles,self.taille_tiles))
    self.corp_ligne = pygame.image.load("asset/murene/murene1.png")
    self.corp_ligne = pygame.transform.scale(self.corp_ligne,(self.taille_tiles,self.taille_tiles))
    self.queue = pygame.image.load("asset/murene/murene3.png")
    self.queue = pygame.transform.scale(self.queue, (self.taille_tiles,self.taille_tiles))
    self.tourner_bas_droit = pygame.image.load("asset/murene/murene2.png")
    self.tourner_bas_droit = pygame.transform.scale(self.tourner_bas_droit, (self.taille_tiles,self.taille_tiles))
    
    self.ecran = pygame.display.set_mode(self.size)
    self.surface_dessin = pygame.Surface((180, 150))
    self.grille = grille
    self.personnage = personnage
    self.nb_tile_x = self.size[0]//self.taille_tiles
    self.nb_tile_y = self.size[1]//self.taille_tiles
    self.centre_x = int((self.nb_tile_x)//2)
    self.centre_y = int((self.nb_tile_y)//2)
    self.max_vertical_centre = len(self.grille) - self.centre_y
    self.max_horizontal_centre = len(self.grille[0]) - self.centre_x
    self.Niveau = Niveau(self)



  def interface_ferme(self) :
    for event in pygame.event.get() :
      if event.type == pygame.QUIT :
        pygame.quit()
        sys.exit()
        return False
    return True

  def analyse_grille(self,sacs):
    #cette fonction a chaque itération permet  d'analyser les cases de la grille
    #et d'appeler les bonnes fonctions pour afficher ce qu'il y a à ces endroits
    self.ecran.fill((0,0,0))
    self.dessine_background()
    for i in range(len(self.grille)):
      for j in range(len(self.grille[i])):
        x,y = self.camera_perso(j, i)
        affiche = self.grille[i][j]

        if affiche <= 20 and affiche >= 10 :
          self.dessine_rocher(x,y, j,i)

        elif affiche == 1:
          self.dessine_perso(x,y)

        elif affiche > 20 and affiche  < 35 :
          self.dessine_serpent(x,y,j,i, affiche)

        elif affiche == 2 :
          self.dessine_sac_poubelle(x,y)

        elif affiche >= 4 and affiche <= 7:
          self.dessine_proj(x,y,affiche)
    self.affiche_score(sacs)
    pygame.display.flip()


  def camera_perso(self, x, y) :
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

  def affiche_score(self,sacs):
    aff_score = self.police.render(str(self.personnage.score)+"/"+str(sacs), True , (255,255,255))
    if len(str(self.personnage.score)+str(sacs)) == 4:
      long_x=120
    elif len(str(self.personnage.score)+str(sacs)) == 3:
      long_x=100
    elif len(str(self.personnage.score)+str(sacs)) == 2:
      long_x=80

    aff_score = pygame.transform.scale(aff_score, (long_x,50))
    self.ecran.blit(aff_score,(600,30))

  def dessine_background(self):
    if self.index <len(self.fond)-1:
      self.index += 0.5
    else:
       self.index = 0

    mx = self.personnage.joueur[0]
    my = self.personnage.joueur[1]

    if mx > self.max_horizontal_centre or mx-  self.centre_x < 0:
      mx = 0
    if my > self.max_vertical_centre or my- self.centre_y < 0:
      my = 0
    for v in range(0,4000,self.tiles_size_fond):
      for b in range(0,4000,self.tiles_size_fond):
          self.ecran.blit( self.fond[int(self.index)],(v-((mx*self.taille_tiles)/3),b-((my*self.taille_tiles)/3)))


  def dessine_serpent(self, x,y,X,Y,pos):
    if pos == 21:
      self.ecran.blit( pygame.transform.rotate(self.tete,90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 22:
      self.ecran.blit(pygame.transform.rotate(self.tete,-90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 23 :
      self.ecran.blit(pygame.transform.rotate(self.tete,-180),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 24:
      self.ecran.blit( self.tete,(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 25 :
      self.ecran.blit(self.corp_ligne,(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 26 :
      self.ecran.blit(pygame.transform.rotate(self.corp_ligne,-90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 27:
      self.ecran.blit( self.tourner_bas_droit,(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 28:
      self.ecran.blit( pygame.transform.rotate(self.tourner_bas_droit,-90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 29:
      self.ecran.blit( pygame.transform.rotate(self.tourner_bas_droit,180),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 30:
      self.ecran.blit( pygame.transform.rotate(self.tourner_bas_droit,90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 31:
      self.ecran.blit( pygame.transform.rotate(self.queue,-90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 32:
      self.ecran.blit( pygame.transform.rotate(self.queue,90),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 33:
      self.ecran.blit( pygame.transform.rotate(self.queue,180),(x*self.taille_tiles,y*self.taille_tiles))
    elif pos == 34:
      self.ecran.blit( self.queue,(x*self.taille_tiles,y*self.taille_tiles))

  def dessine_proj(self,x,y,sens):
    if sens == 4:
      self.ecran.blit( self.epine,(x*self.taille_tiles,y*self.taille_tiles))
    elif sens == 5:
      self.ecran.blit( pygame.transform.rotate(self.epine, 180),(x*self.taille_tiles,y*self.taille_tiles))
    elif sens == 6:

      self.ecran.blit( pygame.transform.rotate(self.epine, -90),(x*self.taille_tiles,y*self.taille_tiles))
    elif sens == 7:
      self.ecran.blit( pygame.transform.rotate(self.epine, 90),(x*self.taille_tiles,y*self.taille_tiles))

  def dessine_rocher(self, x,y, X,Y):
    if Y < len(self.grille)-1:
      if self.grille[Y+1][X]>10 and self.grille[Y+1][X] <= 20 :
        self.ecran.blit( self.rock2,(x*self.taille_tiles,y*self.taille_tiles))
      else:
        self.ecran.blit( self.rock,(x*self.taille_tiles,y*self.taille_tiles))
    else:
      self.ecran.blit( self.rock2,(x*self.taille_tiles,y*self.taille_tiles))

  def dessine_sac_poubelle(self, x,y):
    self.ecran.blit(self.poubelle,(x*self.taille_tiles,y*self.taille_tiles))


  def dessine_perso(self,x,y):
    if self.personnage.direction == "DROITE":
        self.ecran.blit( self.perso_d,(x*self.taille_tiles,y*self.taille_tiles))
    elif self.personnage.direction == "GAUCHE":
        self.ecran.blit( pygame.transform.rotate(self.perso_d, 180),(x*self.taille_tiles,y*self.taille_tiles))
    elif self.personnage.direction == "HAUT":
        self.ecran.blit( pygame.transform.rotate(self.perso_d, 90),(x*self.taille_tiles,y*self.taille_tiles))
    elif self.personnage.direction == "BAS":
        self.ecran.blit( pygame.transform.rotate(self.perso_d, -90),(x*self.taille_tiles,y*self.taille_tiles))

  def fin_de_jeu(self):
    self.ecran.fill((0,0,0))
    texte1 = self.police.render("Game Over ! ", True , (255,255,255))
    self.ecran.blit(texte1,(texte1.get_rect(center = (self.size[0]//2, 150 ))))
    pygame.time.wait(100)
    self.ecran_tempo()

  def mission_completed(self):
    self.ecran.fill((0,0,0))
    texte1 = self.police.render("Mission reussie ! ", True , (255,255,255))

    self.ecran.blit(texte1,(texte1.get_rect(center = (self.size[0]//2, 100 ))))

    texte2 = self.police.render("Score "+ (str(self.personnage.score)),True , (255,255,255))
    self.ecran.blit(texte2,(texte2.get_rect(center = (self.size[0]//2, 150 ))))
    pygame.time.wait(800)
    self.ecran_tempo()

  def ecran_debut(self, animation = True):
    self.ecran.fill((0,0,0))

    pos1 = self.size[0]//2 - 150
    for i in "Bienvenue" :
      self.interface_ferme()
      animation = self.verif_echap_espace(animation)
      texte1 = self.police.render(i, True , (255,255,255))
      self.ecran.blit(texte1,(texte1.get_rect(center = (pos1, 130 ))))
      pygame.display.flip()
      if animation:
        pause = random.randint(20,200)
        pygame.time.wait(pause)
      pos1 += 40
      
    pos2 = self.size[0]//2 - 280
    for i in "dans notre jeux" :
      self.interface_ferme()
      animation = self.verif_echap_espace(animation)
      texte2 = self.police.render(i,True , (255,255,255))
      self.ecran.blit(texte2,(texte2.get_rect(center = (pos2, 180 ))))
      pygame.display.flip()
      if animation :
        pause = random.randint(20,200)
        pygame.time.wait(pause)
      pos2 += 40

    self.ecran_tempo(True)

  def verif_echap_espace(self, animation):
    for event in pygame.event.get():
      if pygame.mouse.get_pressed()[0] :
        return False
    if animation == True :
      return True
    else :
      return False


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
      pygame.display.flip()
      pygame.time.wait(10)


  def ecran_tempo(self,montrer_level = False):
    play = pygame.transform.scale(self.play_button.convert_alpha(), (260,100))
    exit = pygame.transform.scale(self.exit_button.convert_alpha(), (280,120))
    
    play_button_rect = play.get_rect(center = (self.size[0]//2, 300))
    exit_button_react = exit.get_rect(center = (self.size[0]//2, 500 ))
    if  montrer_level :
      score = self.police.render("Score", True , (255,255,255))
      score_react = score.get_rect(center = (self.size[0]//2, 400 ))
      self.ecran.blit(score, score_react)

    self.ecran.blit(play,play_button_rect)
    self.ecran.blit(exit,exit_button_react)
    pygame.display.flip()

    ecran_de_fin = True
    while ecran_de_fin :
      self.interface_ferme()
      pygame.time.Clock().tick(30)
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if play_button_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pressed()[0]:
          pygame.time.delay(200)
        if montrer_level:
          self.Niveau.niveau_montrer()
        else :
          self.jeu = False
        ecran_de_fin = False
        return False

      elif exit_button_react.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:

        pygame.quit()
        sys.exit()

      elif montrer_level and score_react.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] :
        self.ecran.fill((0,0,0))
        text = self.police.render("Les  scores",True , (255,255,255))
        text_rect = text.get_rect(center = (self.size[0]//2, 100))
        self.ecran.blit(text,text_rect)

        smaller_font = pygame.font.Font("asset/ARCADECLASSIC.ttf", 32)
        texte = smaller_font.render("Appyez  sur  echap  pour  lancer le jeu",True,(255,255,255))
        texte_rect = texte.get_rect(center = (self.size[0]//2, 650))
        self.ecran.blit(texte, texte_rect)   

        pos = 250
        with open ("asset/score.txt", 'r') as fichier :
          for i in fichier.readlines():
            texte = self.police.render(i[:-1],True,(255,255,255))
            texte_rect = texte.get_rect(center = (self.size[0]//2, pos))
            self.ecran.blit(texte, texte_rect)
            pos += 75
            pygame.display.flip()
            pygame.time.delay(100)
        while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
          self.interface_ferme()
        ecran_de_fin = False
        self.ecran_debut(False)
        

  

class Niveau():
  def __init__(self, inter):
    self.inter = inter
    self.niveau = 0

  def niveau_montrer(self):
    self.inter.ecran.fill((0,0,0))

    if self.niveau == 0 :
      text = self.inter.police.render("Choisissez",True , (255,255,255))
      text_rect = text.get_rect(center = (self.inter.size[0]//2, 100))
      self.inter.ecran.blit(text,text_rect)

      text2 = self.inter.police.render("votre  niveau",True , (255,255,255))
      text2_rect = text2.get_rect(center = (self.inter.size[0]//2, 150))
      self.inter.ecran.blit(text2,text2_rect)



      niveau1 = self.inter.police.render("Niveau 1",True , (255,255,255))
      niveau1_rect = niveau1.get_rect(center = (self.inter.size[0]//2, 300))
      self.inter.ecran.blit(niveau1,niveau1_rect)

      niveau2 = self.inter.police.render("Niveau 2",True , (255,255,255))
      niveau2_rect = niveau2.get_rect(center = (self.inter.size[0]//2, 400 ))
      self.inter.ecran.blit(niveau2,niveau2_rect)

      niveau3 = self.inter.police.render("Niveau 3",True , (255,255,255))
      niveau3_rect = niveau3.get_rect(center = (self.inter.size[0]//2, 500 ))
      self.inter.ecran.blit(niveau3,niveau3_rect)



      pygame.display.flip()

      while pygame.mouse.get_pressed()[0]:
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
          self.niveau  = 3
        self.inter.interface_ferme()
