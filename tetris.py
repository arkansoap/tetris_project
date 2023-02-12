from random import choice
import pygame, sys
import time
from constantes import *

class PIECES:
    def __init__(self, x, y,r, forme):
        self.x = x
        self.y = y
        self.r = r
        self.forme = forme 
        self.coord_piece()
        self.color_forme()

    def color_forme(self):
        for forme, color in zip(LISTFORME, LISTECOLFORME):
            if forme == self.forme:
                self.color = color

    def coord_piece(self):
        coord_piece = []
        for i, ligne in enumerate(self.forme[self.r]):
            for j, case in enumerate(ligne):
                if case == 1:
                    coord_piece.append([i+self.x, j+self.y])
        self.coords = coord_piece

class JEU: 
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock
        self.screen = pygame.display.set_mode(SIZESCREEN)
        self.begin_surf = pygame.Surface((BEGIN_SURF))
        self.begin_rect = self.begin_surf.get_rect(center = (CENTER_BEGIN))
        self.grid_surf = pygame.Surface((GRIDSURF))
        self.grid_rect = self.grid_surf.get_rect(topleft = (TOPLEFT_GRID))
        self.infos_surf = pygame.Surface((GRIDSURF))
        self.infos_rect = self.grid_surf.get_rect(topleft = (TOPLEFT_INFOS))
        self.infos_surf.fill('Grey')
        self.subInfo_line = pygame.Surface((SUBINFOSURF))
        self.subInfo_line.fill('Blue')
        self.infos_line = self.infos_surf.get_rect(topleft = (TOPLEFT_LINE)) 
        self.subInfo_score = pygame.Surface((SUBINFOSURF))
        self.subInfo_score.fill('Blue')
        self.infos_score = self.infos_surf.get_rect(topleft = (TOPLEFT_SCORE))
        self.subInfos_forme = pygame.Surface((SUBINFOFORME))
        self.subInfos_forme.fill('Blue')
        self.infos_forme = self.infos_surf.get_rect(topleft = (TOPLEFT_FORME))
        self.coord_ground = []
        self.nb_line = 0

    def drawGrid(self, surface):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE,
                                BLOCKSIZE, BLOCKSIZE)
                pygame.draw.rect(surface, 'White', rect, 1)

    def color_square(self, x, y, color, surf):
        rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE,
                            BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(surf, color, rect)

    def print_forme(self, liste, ground, surf):
        for point in liste:
            if ground == True:
                self.color_square(point[0][0], point[0][1], point[1], surf)
            else:
                self.color_square(point[0], point[1], self.piece.color, surf)

    def get_piece(self, x, y,r, forme):
        piece = PIECES(x,y,r,forme)
        self.piece = piece
        self.derniere_chute = time.time()
        self.newpiece = PIECES(INIT_X,INIT_Y,0,choice(LISTFORME))

    def new_piece(self):
        self.piece=self.newpiece
        self.derniere_chute = time.time()
        self.newpiece = PIECES(INIT_X,INIT_Y,0,choice(LISTFORME))

    def moove_gauche_valide(self):
        for coord in self.piece.coords:
            if coord[0]<1:
                return False
        else: return True

    def moove_droit_valide(self):
        for coord in self.piece.coords:
            if coord[0]>GRID_WIDTH-2:
                return False
        else: return True

    def fond_valide(self):
        for coord in self.piece.coords:
            if coord[1]>GRID_HEIGHT-2:
                return False
        else: return True

    def rotation_valide(self):
        pass
        
    def collision_horizontale(self):
        for coord in self.piece.coords:
            for coord2 in self.coord_ground:
                if coord[1] == coord2[0][1] and (coord[0]-1 == coord2[0][0] or coord[0]+1 == coord2[0][0]):
                    return False
        else: return True

    def collision_verticale(self):
        for coord in self.piece.coords:
            for coord2 in self.coord_ground:
                if coord[0] == coord2[0][0] and coord[1]+1 == coord2[0][1]:
                    return False
        else: return True

    def suppression_ligne(self):
        linesup=0
        compteur = 0
        for i in range(GRID_HEIGHT):
            compteur = 0
            for point in self.coord_ground:
                if point[0][1] == i:
                    compteur += 1
            if compteur == GRID_WIDTH:
                print("line")
                linesup +=1
                self.nb_line +=1
                for point in self.coord_ground[:]:
                    if point[0][1]==i:
                        self.coord_ground.remove(point)
                for a, point in enumerate(self.coord_ground):
                    if point[0][1]<i:
                        self.coord_ground[a] = [[point[0][0], point[0][1] +1],point[1]]
        return linesup

    def gerer_gravite(self):
        if time.time() - self.derniere_chute > GRAVITE:
            self.derniere_chute = time.time()
            if self.fond_valide() and self.collision_verticale():
                self.piece.y +=1
                self.piece.coord_piece()
            else:
                for point in self.piece.coords:
                    self.coord_ground.append([point,self.piece.color])
                    self.detecte_fin()
                self.new_piece()

    def detecte_fin(self):
        for coord in self.coord_ground:
            if coord[0][0] == 1:
                On_game == False

    def slide_bar(self):
        myfont = pygame.font.SysFont("Black", 32,True)
        myfont2 = pygame.font.SysFont("Black", 18,False)
        score_display = myfont.render(str(self.nb_line), 1, (255,255,255))
        titre_score = myfont2.render("Nombre de lignes",1, (255,255,255))
        titreLineRect = titre_score.get_rect(center = (SUBINFOSURF[0]//2-10,SUBINFOSURF[1]//4))
        self.infos_surf.fill('Grey')
        self.screen.blit(self.infos_surf, self.infos_rect)
        self.screen.blit(self.subInfo_line, self.infos_line)
        self.screen.blit(self.subInfo_score, self.infos_score)
        self.screen.blit(self.subInfos_forme, self.infos_forme)
        self.subInfo_line.fill('Blue')
        self.subInfo_line.blit(titre_score, titreLineRect)
        self.subInfo_line.blit(score_display,(SUBINFOSURF[0]//2-10,SUBINFOSURF[1]//2 -10))
        self.subInfos_forme.fill('Blue')
        for point in self.newpiece.coords:
            self.color_square(point[0]-3, point[1], self.newpiece.color, self.subInfos_forme)
        self.drawGrid(self.subInfos_forme)


    def affichage(self):      
        self.grid_surf.fill('Grey')
        self.print_forme(self.piece.coords, False, self.grid_surf )
        self.suppression_ligne()
        if self.coord_ground != []:
            self.print_forme(self.coord_ground, True, self.grid_surf)
        self.drawGrid(self.grid_surf)
        self.screen.blit(self.grid_surf, self.grid_rect)
        self.slide_bar()

    def gerer_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.moove_droit_valide() and self.collision_horizontale():
                        self.piece.x += 1
                        self.piece.coord_piece()
                if event.key == pygame.K_LEFT:
                    if self.moove_gauche_valide() and self.collision_horizontale():
                        self.piece.x -=1
                        self.piece.coord_piece()
                if event.key == pygame.K_UP:
                    r = self.piece.r
                    if r+1 > len(self.piece.forme)-1: #entrer le rmax ds ini de PIECES
                        self.piece.r = 0
                    else:
                        #calculer coord de rotation suivante
                        #regarder si coord valide (pas occupée)
                         self.piece.r += 1 
                if event.key == pygame.K_DOWN:
                    if self.fond_valide() and self.collision_verticale():
                        self.piece.y +=1
                        self.piece.coord_piece()
    
    def affiche_begin(self):
        myfont2 = pygame.font.SysFont("Blue", 40,False)
        titre_begin = myfont2.render("The Flex Begin",1, "White")
        titreBeginRect = titre_begin.get_rect(center = (CENTER_BEGIN))
        self.begin_surf.fill("Blue")
        self.screen.blit(self.begin_surf, self.begin_rect)
        self.screen.blit(titre_begin, titreBeginRect)
        pygame.display.update()
        pygame.time.wait(3000)
        self.screen.fill("Black")
        
    def affiche_end(self):
        pass

    def init_game(self):
        self.drawGrid(self.grid_surf)
        self.get_piece(INIT_X,INIT_Y,0,choice(LISTFORME)) 
        self.print_forme(self.piece.coords, self.piece.color, self.grid_surf)
        self.screen.blit(self.grid_surf, self.grid_rect)

    def play(self):
        On_game = True
        self.init_game()
        while On_game is True:
            self.gerer_event()
            self.gerer_gravite()
            self.affichage()
            pygame.display.update()

if __name__ == '__main__':
    J = JEU()
    J.affiche_begin()
    J.play()