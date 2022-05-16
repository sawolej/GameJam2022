import pygame
import sys

class MapaWyboru:
    def __init__(self,game):
        self.obrazki = []
        self.lista_rect = []
        self.uchwyt_gra = game
        self.background = pygame.image.load("Tekstury/mapa_wyboru.png")
        self.obrazki.append(pygame.image.load("Tekstury/camille_symbol.png"))
        self.obrazki.append(pygame.image.load("Tekstury/durlique_symbol.png"))
        self.obrazki.append(pygame.image.load("Tekstury/muszal_symbol.png"))
        self.obrazki.append(pygame.image.load("Tekstury/wolfenn_symbol.png"))
        self.obrazki.append(pygame.image.load("Tekstury/henryk_symbol.png"))
        for i in range(0,5):
            self.obrazki[i] = pygame.transform.scale(self.obrazki[i],(50,50))
            self.lista_rect.append(self.obrazki[i].get_rect())

        """
        self.background = pygame.image.load("Tekstury/mapa_wyboru.png")
        self.camille_symbol = pygame.image.load("Tekstury/camille_symbol.png")
        self.camille_symbol_rect = self.background.get_rect()
        self.durilique_symbol = pygame.image.load("Tekstury/durlique_symbol.png")
        self.durilique_symbol_rect = self.durilique_symbol.get_rect()
        self.muszal_symbol = pygame.image.load("Tekstury/muszal_symbol.png")
        self.muszal_symbol_rect = self.muszal_symbol.get_rect()
        self.wolfenn_symbol = pygame.image.load("Tekstury/wolfenn_symbol.png")
        self.wolfenn_symbol_rect = self.wolfenn_symbol.get_rect()
        self.henryk_symbol = pygame.image.load("Tekstury/henryk_symbol.png")
        self.henryk_symbol_recy = self.henryk_symbol.get_rect()
        """
    def start_mapa_wyboru(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.uchwyt_gra.settings.hsp[1] != 700:
                self.uchwyt_gra.state = "opis_poziomu"
            if keys[pygame.K_w] and self.uchwyt_gra.settings.mozliwe_ruchy[0] == 1:
                if self.uchwyt_gra.settings.hsp[1] == 700:
                    self.uchwyt_gra.settings.mozliwe_ruchy = [0,0,1,1]
                    self.uchwyt_gra.settings.hsp[1] = 510
                if self.uchwyt_gra.settings.hsp[0] == 780 and self.uchwyt_gra.settings.hsp[1] == 370:
                    self.uchwyt_gra.settings.mozliwe_ruchy = [1, 0, 1, 1]
                    self.uchwyt_gra.settings.hsp = [575,235]
                if self.uchwyt_gra.settings.hsp[0] == 370 and self.uchwyt_gra.settings.hsp[1] == 370:
                    self.uchwyt_gra.settings.mozliwe_ruchy = [1, 0, 1, 1]
                    self.uchwyt_gra.settings.hsp = [575, 235]
                if self.uchwyt_gra.settings.hsp[1] == 235 and self.uchwyt_gra.settings.final == 1:
                    self.uchwyt_gra.settings.hsp = [575, 50]
            if keys[pygame.K_s] and self.uchwyt_gra.settings.mozliwe_ruchy[1] == 1:
                if self.uchwyt_gra.settings.hsp[0] == 780 and self.uchwyt_gra.settings.hsp[1] == 370:
                    self.uchwyt_gra.settings.mozliwe_ruchy = [0, 0, 1, 1]
                    self.uchwyt_gra.settings.hsp = [575,510]
                if self.uchwyt_gra.settings.hsp[0] == 370 and self.uchwyt_gra.settings.hsp[1] == 370:
                    self.uchwyt_gra.settings.mozliwe_ruchy = [0, 0, 1, 1]
                    self.uchwyt_gra.settings.hsp = [575,510]
            if keys[pygame.K_a] and self.uchwyt_gra.settings.mozliwe_ruchy[2] == 1:
                self.uchwyt_gra.settings.hsp = [370,370]
                self.uchwyt_gra.settings.mozliwe_ruchy = [1, 1, 0, 0]
            if keys[pygame.K_d] and self.uchwyt_gra.settings.mozliwe_ruchy[3] == 1:
                self.uchwyt_gra.settings.hsp = [780, 370]
                self.uchwyt_gra.settings.mozliwe_ruchy = [1, 1, 0, 0]



            # odwierzanie ekranu w trakcie iteracji petli
        self.uchwyt_gra.screen.blit(self.background,(0,0))
        self.uchwyt_gra.screen.blit(self.obrazki[0],(self.uchwyt_gra.settings.csp[0],self.uchwyt_gra.settings.csp[1]))
        self.uchwyt_gra.screen.blit(self.obrazki[1] ,(self.uchwyt_gra.settings.dsp[0],self.uchwyt_gra.settings.dsp[1]))
        self.uchwyt_gra.screen.blit(self.obrazki[2],(self.uchwyt_gra.settings.msp[0],self.uchwyt_gra.settings.msp[1]))
        self.uchwyt_gra.screen.blit(self.obrazki[3],(self.uchwyt_gra.settings.wsp[0],self.uchwyt_gra.settings.wsp[1]))
        self.uchwyt_gra.screen.blit(self.obrazki[4] ,(self.uchwyt_gra.settings.hsp[0],self.uchwyt_gra.settings.hsp[1]))