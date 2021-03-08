import pygame
import random
from grille import Grille
                
pygame.init()
morpion = Grille()
morpion.quadrillage()

croix = morpion.image("croix.png")
rond = morpion.image("rond.png")

run = True
game = 0
i = 0
r = 0
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        
        if r == 0:
            morpion.text("Joueur vs Joueur : Touche J", -60, 50)
            morpion.text("Joueur vs Ordinateur : Touche O", 60, 50)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    game = 0
                    r = 1
                    morpion.quadrillage()
                if event.key == pygame.K_o:
                    game = 1
                    r = 1
                    morpion.quadrillage()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                pos = pygame.mouse.get_pos()
                c = morpion.centre(pos)
                x = morpion.case(pos)
                
                if i%2 == 0:
                    if morpion.grid[x] == x:
                        morpion.surf.blit(croix, c)
                        morpion.cocher(pos, i)
                else:
                    if morpion.grid[x] == x:
                        morpion.surf.blit(rond, c)
                        morpion.cocher(pos, i)
                  
                print(morpion.etat_jeu()) 
                if i%2 == 0:
                    if morpion.gagnant(morpion.grid, i):
                        morpion.win_text(1)
                        pygame.display.flip()
                        pygame.time.wait(2500)
                        morpion.restart()
                        i = 0
                        r = 0
                    else:
                        i+=1
                else:
                    if morpion.gagnant(morpion.grid, i):
                        morpion.win_text(2)
                        pygame.display.flip()
                        pygame.time.wait(2500)
                        morpion.restart()
                        i = 0
                        r = 0
                    else:
                        i+=1
                        
    if i%2 != 0 and game == 1:
        pygame.display.flip()
        pygame.time.wait(500)
        l = morpion.cases_vides()
        if l:
            a = random.choice(l)
            c = morpion.pos_case(a)
            morpion.surf.blit(rond, c)
            morpion.changer_grille(a, morpion.tour("X", "O", i))
        i+=1
    
    if morpion.nul(morpion.grid):
        morpion.text("Match Nul")
        pygame.display.flip()
        i = 0
        r = 0
        pygame.time.wait(2500)
        morpion.restart()
        
    
    
        
                
    
    pygame.display.flip()

pygame.quit()