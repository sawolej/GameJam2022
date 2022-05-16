import pygame
from pygame import mixer
import math
import screenscroll as sc
aktualna_scena = 0
def level_one(game):
    mixer.music.load("salt.wav")
    mixer.music.play(-1)
    uchwyt_gra = game
    #bullet - walka wręcz
    #bulletK - pocisk cienia
    pygame.init()
    vec = pygame.math.Vector2
    width = 1200
    height=800
    win = pygame.display.set_mode((width, height))

    pygame.display.set_caption("First Game")
    fireS = pygame.image.load('Tekstury/fire.png')
    claws = pygame.image.load('Tekstury/claws.png')
    claws = pygame.transform.scale(claws,(100,100))
    walkRight = pygame.image.load('Tekstury/henrykRight.png')
    walkRight = pygame.transform.scale(walkRight,(100,150))
    walkLeft = pygame.image.load('Tekstury/henrykLeft.png')
    walkLeft = pygame.transform.scale(walkLeft,(100,150))
    bg_all = pygame.image.load('Tekstury/bg_all.png')
    bg_all = pygame.transform.scale(bg_all,(3600,800))
    brighten = 128
    brighten_two = 1
    wschod_slonca = 35
    sila_slonca = 0
    bg_all.fill((brighten, brighten, brighten),special_flags=pygame.BLEND_RGB_SUB)
    #bg = pygame.image.load('Tekstury/bg.png')
    #gr = pygame.image.load('Tekstury/gr.png')
    #niebo = pygame.image.load('Tekstury/niebo_01.png')
    #bg = pygame.transform.scale(bg,(3000,600))
    #gr = pygame.transform.scale(gr,(3000,1000))
    #niebo = pygame.transform.scale(niebo,(1000,1000))
    char = pygame.image.load('Tekstury/henrykRight.png')
    wspinable = False
    clock = pygame.time.Clock()
    ilosc_scen = 4
    ak_sc = 0





    class objLight(object):
        def __init__(self, x, y):

            self.x = x
            self.y = y
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            self.visible = True
        def draw(self, win):
            if self.visible:
                win.blit(fireS, (self.x, self.y))

        def hit(self):
            self.visible = False


    score = 0


    class player(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.standing = True
            self.health = 200
            self.hitbox = (self.x , self.y , 29, 52)
            self.image = walkLeft
            self.rect = self.image.get_rect()
            self.ground_y = 100
            self.smierc = 0

        def get_damage(self, amount):
            if self.health > 0:
                self.health -= amount
            if self.health <= 0:
                self.background = pygame.image.load("Tekstury/smierc.png")
                win.blit(self.background, (0, 0))
                pygame.display.flip()
                while True:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        break
                self.smierc = 1


        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not (self.standing):
                if self.left:
                    win.blit(walkLeft, (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight, (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight, (self.x, self.y))
                else:
                    win.blit(walkLeft, (self.x, self.y))
            self.hitbox = (self.x , self.y, 0, 52)
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            sc.move(self)

            #if self.x == 1100:
             #   self.x = 0


    class projectile(object):
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


    class enemy(object):
        walkRight = pygame.image.load('Tekstury/chopRight.png')

        walkLeft = pygame.image.load('Tekstury/chopLeft.png')

        def __init__(self, x, y, width, height, end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [self.x, self.end]
            self.walkCount = 0
            self.vel = 3
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            self.health = 10
            self.visible = True

            self.rect_left = pygame.Rect((x, y), (2, height))
            self.rect_right = pygame.Rect((x, y + width - 2), (2, height))

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.walkRight, (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft, (self.x, self.y))
                    self.walkCount += 1

                pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = (self.x + 17, self.y + 2, 31, 57)
                # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
        def hit(self):
            if self.health > 0:
                self.health -= 1
                man.health += 5
            else:
                self.visible = False
            print('hit')

        def attack_player(self,player):
            distan = player.x - self.x
            if distan <= self.attack_range:
                # zabawa z colission
                # pass
                if self.WalkRight and pygame.Rect.colliderect(self.rect_right, player.rect): player.health -= self.damage
                if self.WalkLeft and pygame.Rect.colliderect(self.rect_left, player.rect): player.health -= self.damage

            # player.health = player.health - self.damage

        def detect_player(self,player):
            distan = player.x - self.x
            if distan <= self.vision_range:
                if self.right:
                    self.attack_player()
            if distan <= self.vision_range:
                if self.left:
                    pass
                else:
                    self.attack_player()

    def redrawGameWindow(aktualna_scena):
        #win.blit(niebo, (0, 0))
        #win.blit(bg, (0, 0))
        if aktualna_scena == 0:
            win.blit(bg_all, (0, 0))
        if aktualna_scena == 1:
            win.blit(bg_all, (0, 0))
            chopi[0].draw(win)
            objLight(250, 410).draw(win)
            chopi[1].draw(win)
        if aktualna_scena == 2:
            win.blit(bg_all, (0, 0))
        if aktualna_scena == 3:
            fire.draw(win)
            win.blit(bg_all, (-1200, 0))
        if aktualna_scena == 4:
            win.blit(bg_all, (0, 0))
        if aktualna_scena == 5:
            win.blit(bg_all, (-1200, 0))
        if aktualna_scena == 6:
            win.blit(bg_all, (-2400, 0))
            chopi[2].draw(win)
            chopi[3].draw(win)
            chopi[4].draw(win)
            chopi[5].draw(win)
        if aktualna_scena == 7:
            win.blit(bg_all, (-2400, 0))
            chop.draw(win)
        if aktualna_scena == 8:
            background = pygame.image.load("Tekstury/Epilog.png")
            win.blit(background, (0, 0))
            pygame.display.flip()
            while True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    break

        print(aktualna_scena)
        #win.blit(gr, (0, 550))
        text = font.render('Score: ' + str(score), 1, (0, 0, 0))
        win.blit(text, (550, 10))
        man.draw(win)
        for bulletK in bulletsK:
            bulletK.draw(win)

        #pygame.display.update()

    font = pygame.font.SysFont('comicsans', 30, True)

    man = player(50, 410, 64, 64)
    chop = enemy(100, 410, 64, 64, 450)
    chopi = [enemy(100, 410, 64, 64, 450), enemy(400, 410, 64, 64, 450), enemy(100, 410, 64, 64, 450),
             enemy(200, 410, 64, 64, 450),
             enemy(300, 410, 64, 64, 450), enemy(500, 410, 64, 64, 450)]
    fire = objLight(500, 410)
    shootLoop = 0
    bullets = []
    bulletsK = []
    while man.smierc==0:
        clock.tick(27)

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bulletK in bulletsK:
            if bulletK.y - bulletK.radius < fire.hitbox[1] + fire.hitbox[3] and bulletK.y + bulletK.radius > fire.hitbox[
                1]:

                    fire.visible = False

                    #pygame.display.update()
                    bulletsK.pop(bulletsK.index(bulletK))

        for bullet in bullets:
            if bullet.y - bullet.radius < chop.hitbox[1] + chop.hitbox[3] and bullet.y + bullet.radius > chop.hitbox[
                1] and man.x - chop.x <20:
                if bullet.x + bullet.radius > chop.hitbox[0] and bullet.x - bullet.radius < chop.hitbox[0] + \
                        chop.hitbox[2]:
                    chop.hit()
                    if chop.visible:
                        print("dupa")
                        win.blit(claws, (man.x, man.y))
                    #pygame.display.update()
                    score += 1
                    bullets.pop(bullets.index(bullet))

            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        for bulletK in bulletsK:
            if bulletK.x < 500 and bulletK.x > 0:
                bulletK.x += bulletK.vel
            else:
                bulletsK.pop(bulletsK.index(bulletK))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_k] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bulletsK) < 5:
                bulletsK.append(
                    projectile(round(man.x + man.width // 2), round(man.y + 60), 6, (0, 0, 0), facing))
            shootLoop = 1

        if keys[pygame.K_j] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(
                    projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

            shootLoop = 1

        if keys[pygame.K_a] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_d] and man.x < width - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0
        if keys[pygame.K_RSHIFT]:
            if man.right:
                man.x +=40
                man.right = True
                man.left = False
                man.standing = False

            else:
                man.x-=40
                man.left = True
                man.right = False
                man.standing = False
        if not (man.isJump):
            if keys[pygame.K_SPACE]:
                man.isJump = True

        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
        if pygame.time.get_ticks()%wschod_slonca == 0:
            if wschod_slonca > 8:
                wschod_slonca-=1
            bg_all.fill(( brighten_two ,  brighten_two ,  brighten_two ), special_flags=pygame.BLEND_RGB_ADD)
            if wschod_slonca < 15:
                sila_slonca+=1
        man.get_damage(sila_slonca)

        if man.x > 1100:
            man.x = 0
            ak_sc = ak_sc + 1
        redrawGameWindow(ak_sc)
        #pygame.display.update()
        box = pygame.Rect(10, 10, man.health, 50)
        pygame.draw.rect(win, (0, 150, 255), box)
        pygame.display.flip()

    pygame.quit()