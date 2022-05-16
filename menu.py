import pygame
import sys

class Menu():
    def __init__(self,game):
        self.nastepny_stan = "prolog"
        self.uchwyt_gra = game

    def start_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                 self.uchwyt_gra.state = self.nastepny_stan

        # odwierzanie ekranu w trakcie iteracji petli
        self.uchwyt_gra.screen.fill((230, 230, 230))