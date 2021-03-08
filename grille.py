import pygame
from ia import Ia
class Grille:
    
    def __init__(self, largeur=600, hauteur=600, grid=[0, 1, 2, 3, 4, 5, 6, 7, 8], base=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        """ Initialisation de la fenêtre de jeu """
        self.largeur = largeur
        self.hauteur = hauteur
        self.surf = pygame.display.set_mode((largeur,hauteur))
        self.police = pygame.font.Font(None,72)
        self.grid = grid
        self.base = base  
        
    def quadrillage(self):
        """ Trace le quadrillage du morpion
        largeur, hauteur: entiers définissant les dimensions de la fenêtre"""
        largeur = self.largeur
        hauteur = self.largeur
        surf = self.surf
        largeur1 = largeur/3
        largeur2 = largeur - largeur1
    
        hauteur1 = hauteur/3
        hauteur2 = hauteur - hauteur1
        
        surf.fill((255,255,255))
        
        pygame.draw.line(surf,(0,0,0),(largeur1, 0),(largeur1, hauteur),2)
        pygame.draw.line(surf,(0,0,0),(largeur2, 0),(largeur2, hauteur),2)
        
        pygame.draw.line(surf,(0,0,0),(0, hauteur1),(largeur, hauteur1),2)
        pygame.draw.line(surf,(0,0,0),(0, hauteur2),(largeur, hauteur2),2)
    
    def etat_jeu(self):
        return self.grid
    
    def cases_vides(self):
        l = []
        for x in self.grid:
            if type(x) == int:
                l.append(x)
        return l
    
    def ordi(self,i):
        ia = Ia()
        l = self.cases_vides()
        score = 0
        for x in l:
            ia.ajouter_coup(self.grid[x])
        for y in ia.coups:    
            test = self.grid
            test[y] = "O"
            if self.gagnant(test, i):
                score = 1
            elif self.nul(test):
                score = 0
            else:
                score = -1
        ia.ajouter_score(score)
        c = ia.meilleur_score()
        a = ia.scores.index(c)
        return a
    
    def changer_grille(self, i, y):
        self.grid[i] = y
        return self.grid
    
    def win(self, i):
        if i%2 == 0:
                self.win_text(1)
                pygame.display.flip()
                pygame.time.wait(2400)
        else:
                self.win_text(2)
                pygame.display.flip()
                pygame.time.wait(2400)
        return i
    
    def restart(self):
        self.grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.quadrillage()
        return self.grid
          
    
    def pos_case(self, c):
        """ Renvoie les coordonnées du milieu de la case donnée """
        hauteur, largeur = self.hauteur, self.largeur
        x, y = 0, 0
        if c == 0:
            x, y = 0, 0
        if c == 3:
            x, y = 0, hauteur/3
        if c == 6:
            x, y = 0, hauteur-(hauteur/3)
        if c == 1:     
            x, y = largeur/3, 0
        if c == 4:
            x, y = largeur/3, hauteur/3
        if c == 7:
            x, y = largeur/3, hauteur-(hauteur/3)
        if c == 2:
            x, y = largeur-(largeur/3), 0
        if c == 5:
            x, y = largeur-(largeur/3), hauteur/3
        if c == 8:
            x, y = largeur-(largeur/3), hauteur-(hauteur/3)
        
        return x, y
    
    def cocher(self, pos, i):
         self.grid[self.case(pos)] = self.tour("X", "O", i)
        
    def gagnant(self, grid, i):
        """ Détermine si un joueur a gagné ou non
        i: entier déterminant quel joueur joue ce tour """
        s = self.tour("X", "O", i)    
        situations = [
         [0,1,2],
         [3,4,5],
         [6,7,8],
    
         [0,3,6],
         [1,4,7],
         [2,5,8],
         
         [0,4,8],
         [6,4,2]
        ]
        for x in situations:
            if grid[x[0]] == s and grid[x[1]] == s and grid[x[2]] == s:
                return True
            
        return False
    
    def nul(self, grid):
        for i in grid:
            if isinstance(i, int):
                return False
        return True
    
    def centre(self, pos):
        """ Renvoie les coordonnées de la case la plus proche du clic
            pos: tuple contenant les coordonnées x,y de la souris
            largeur, hauteur: entiers définissant les dimensions de la fenêtre """
        x, y= 0, 0
        x1, y1 = pos[0], pos[1]
        largeur = self.largeur
        hauteur = self.largeur
        
        if x1 < largeur/3:
            if y1 < hauteur/3:
                x, y = 0, 0
            elif y1 > hauteur/3 and y1 < hauteur-(hauteur/3):
                x, y = 0, hauteur/3
            elif y1 > hauteur-(hauteur/3):
                x, y = 0, hauteur-(hauteur/3)
                
        elif x1 > largeur/3 and x1 < largeur-(largeur/3):
            if y1 < hauteur/3:
                x, y = largeur/3, 0
            elif y1 > hauteur/3 and y1 < hauteur-(hauteur/3):
                x, y = largeur/3, hauteur/3
            elif y1 > hauteur-(hauteur/3):
                x, y = largeur/3, hauteur-(hauteur/3)
                
        elif x1 > largeur-(largeur/3):
            if y1 < hauteur/3:
                x, y = largeur-(largeur/3), 0
            elif y1 > hauteur/3 and y1 < hauteur-(hauteur/3):
                x, y = largeur-(largeur/3), hauteur/3
            elif y1 > hauteur-(hauteur/3):
                x, y = largeur-(largeur/3), hauteur-(hauteur/3)
                
        return x, y
    
    def case(self, pos):
        largeur = self.largeur
        hauteur = self.largeur
        c = 0
        x1, y1 = pos[0], pos[1]
        
        if x1 < largeur/3:
            if y1 < hauteur/3:
                c = 0
            elif y1 > hauteur/3 and y1 < hauteur-(hauteur/3):
                c = 3
            elif y1 > hauteur-(hauteur/3):
                c = 6
                
        elif x1 > largeur/3 and x1 < largeur-(largeur/3):
            if y1 < hauteur/3:
                c = 1
            elif y1 > hauteur/3 and y1 < hauteur-(hauteur/3):
                c = 4
            elif y1 > hauteur-(hauteur/3):
                c = 7
                
        elif x1 > largeur-(largeur/3):
            if y1 < hauteur/3:
                c = 2
            elif y1 > hauteur/3 and y1 < hauteur-(hauteur/3):
                c = 5
            elif y1 > hauteur-(hauteur/3):
                c = 8
                
        return c
    
    def image(self, img):
        return pygame.image.load(img).convert_alpha()
    
    def text(self, texte, x=0, taille=0, color="#000000"):
        if taille == 0:
            police = self.police
        else:
            police = pygame.font.Font(None,taille)
        text = police.render(texte,True,pygame.Color(color))
        if x == 0:
            text_rect = text.get_rect(center=(self.largeur/2, self.hauteur/2))
        else:
            text_rect = text.get_rect(center=(self.largeur/2, (self.hauteur/2+x)))
        return self.surf.blit(text, text_rect)
    
    def win_text(self, j, color="#000000"):
        text = self.police.render("Le joueur "+ str(j) +" a gagné",True,pygame.Color(color))
        text_rect = text.get_rect(center=(self.largeur/2, self.hauteur/2))
        return self.surf.blit(text, text_rect)
        
    def tour(self, s1, s2, i):
        if i%2 == 0:
            return s1
        else:
            return s2
        