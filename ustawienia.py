
class Ustawienia:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ustawienia z mapy wyboru
        self.csp = [575,235]
        self.dsp = [575,510]
        self.msp = [780,370]
        self.wsp = [370,370]
        self.hsp = [575,700]
        # up,down , left ,right
        self.mozliwe_ruchy = [1,0,0,0]
        #Czy odblokowane finałowe starcie
        self.final = 0