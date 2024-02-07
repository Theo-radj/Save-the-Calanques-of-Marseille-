import snake1
#import snake2
import snake3


class level_snake():
    def __init__(self):
        pass

    def choisir_snake(self,level, grille, personnage, inter):
        if level == 1:
            Snake = snake1.Snake(grille, personnage, inter)
            print("1")
            print(Snake.taille)
            return Snake 
        elif level == 2:
            Snake = snake2.Snake(grille, personnage)
            return Snake
        elif level == 3:
           Snake = snake3.Snake(grille, personnage)
           print(3)
           return Snake
