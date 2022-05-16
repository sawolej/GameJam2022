import sys
import pygame

class OpisPoziomu():
    def __init__(self,game):
        self.uchwyt_gra = game
        self.tekst_do_wyswietlenia = ""
        self.uchwyt_gra.state_box = ""
        self.dlugosc_tekstu=0
        self.numer_litery = 0


    def start_opis_poziomu(self):
        if self.tekst_do_wyswietlenia == "":
            if self.uchwyt_gra.settings.hsp == [575, 510]:
                self.tekst_do_wyswietlenia="Góry Mgliste \n Skute lodem góry w których zima zdaje się nigdy nie kończyć. \n Noc wciąż jest wystarczająco długa a skaliste szczyty. \n zapewniają wystarczająco cienia byśmy mogli bezpiecznie się przemieszczać.\n Atoli wolimy nie nadużywać naszego szczęścia."
                self.uchwyt_gra.state_box = "level_threeddddd"
                self.background = pygame.image.load("Tekstury/zwoj_opis_gory.png")
            if self.uchwyt_gra.settings.hsp == [575,235]:
                self.tekst_do_wyswietlenia ="Fallwood \n Największe miasto w regionie. Robimy się głodni na myśl o tych wszystkich ludziach pościskanych tam jak ryby w puszcze. Tak długo jak będziemy przemieszczać pod dachami i kanałami będziemy bezpieczni. Tak długo jak nie spotkamy magów."
                self.uchwyt_gra.state_box = "level_four"
                self.background = pygame.image.load("Tekstury/zwoj_fallwood.png")
            if self.uchwyt_gra.settings.hsp == [780,370]:
                self.tekst_do_wyswietlenia = "Retcon Wiocha. - Bezimienna wioska \n Nazwy wsi takich jak te zostały zapomniane przez wszystkich, włącznie z ich mieszkańcami. Na dobrą sprawę kilka zbitych ze sobą spróchniałymi dechami chałup ciężko nazwać wsią. Jednakże kapłani Heliosa czyhają i tutaj. A to oznacza że jesteśmy tu i My. "
                self.uchwyt_gra.state_box = "level_one"
                self.background = pygame.image.load("Tekstury/zwoj_wioska.png")
            if self.uchwyt_gra.settings.hsp == [370,370]:
                self.tekst_do_wyswietlenia ="Stare Mokradła \n Bagniska zaczynają odmarzać i wypełniają nasze nozdrza ogłuszającym smrodem. Nawet najciemniejsze segmenty Syèl la nie były tak paskudne. Na szczęście bagno oferuje wiele jaskiń i leśnych gęstwin by ukryć się przed światłem. "
                self.uchwyt_gra.state_box = "level_two"
                self.background = pygame.image.load("Tekstury/zwoj_staremokradla.png")
            if self.uchwyt_gra.settings.hsp == [575, 50]:
                self.tekst_do_wyswietlenia = " Pustynia Kabira \n Nareszcie! Mamy wszystkie artefakty! Dawno nie czuliśmy takiej ekscytacji, jednak najgorsze przed nami. Jedno miejsce ma wystarczająco nagromadzonej esencji Syèli i jest to świątynia w sercu pustyni. Będziemy gonić się z czasem, a na miejscu bez wątpienia będą chcieli powstrzymać nas Helianie. Musimy być pewni że jesteśmy gotowi."
                self.uchwyt_gra.state_box = "level_final"
                self.background = pygame.image.load("Tekstury/zwoj_opis_pustynia.png")
            self.dlugosc_tekstu = len(self.tekst_do_wyswietlenia)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.uchwyt_gra.state = self.uchwyt_gra.state_box
            elif keys[pygame.K_ESCAPE]:
                self.tekst_do_wyswietlenia = ""
                self.uchwyt_gra.state = "mapa_wyboru"
        self.uchwyt_gra.screen.blit(self.background, (0, 0))
