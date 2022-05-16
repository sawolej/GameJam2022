import sys
import pygame
import ustawienia as us
#import poziomy as po
import mapa_wyboru as mawy
import opis_poziomu as op
import menu as me
import level_one as lo
import prolog as pro
import smierc as sm

class HomeSick:
    """Ogolna klasa do zarządzania grą """
    def __init__(self):
        pygame.init()
        self.settings = us.Ustawienia()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.state = "menu"
        self.game_menu = me.Menu(self)
        self.game_prolog = pro.Prolog(self)
        self.game_smierc = sm.Smierc(self)
        self.game_opis_poziomu = op.OpisPoziomu(self)
        self.game_mapa_wyboru = mawy.MapaWyboru(self)
        pygame.display.set_caption("HomeSick")

    """Menadżer zarządzania poziomami"""
    def state_menager(self):
        if self.state == "menu":
            self.game_menu.start_menu()
        if self.state == "prolog":
            self.game_prolog.start_prolog()
        if self.state == "smierc":
            self.game_smierc.start_smierc()
        if self.state == "mapa_wyboru":
            self.game_mapa_wyboru.start_mapa_wyboru()
        if self.state == "opis_poziomu":
            self.game_opis_poziomu.start_opis_poziomu()
        if self.state == "level_one":
            lo.level_one(self)
            if self.state == "smierc":
                self.game_smierc.start_smierc()
            self.state = "mapa_wyboru"

        # wyswietlanie ostatnio zmodyfikowanego obrazu
        pygame.display.flip()

    def startowanko(self):
        while True:
            self.state_menager()
        click.tick(60)

if __name__ == "__main__":
    gra = HomeSick()
    gra.startowanko()
