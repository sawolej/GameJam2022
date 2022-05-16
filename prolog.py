import pygame
class Prolog:
    def __init__(self,game):
        self.nastepny_stan = "mapa_wyboru"
        self.uchwyt_gra = game
    def start_prolog(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.uchwyt_gra.state = self.nastepny_stan
        self.background = pygame.image.load("Tekstury/prolog.png")
        self.uchwyt_gra.screen.blit(self.background, (0, 0))