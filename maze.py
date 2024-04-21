from pygame import *
from PyQt5.QtWidgets import (QPushButton)
#from tkinter import *  
import random
walll1 = random.randint(30,90)
#    walll2 = random.randint(sa,se)
m = 0
v = 1
b = 1
nbv = 0
live = 5
#int(input("Сколько жизней ты выберешь(до 5)"))

blue = 255
green = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_sprite, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale( image.load(player_sprite), (65, 65) )
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

'''Класс Игрока'''
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[ K_LEFT ] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[ K_UP ] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[ K_RIGHT ] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[ K_DOWN ] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

'''Класс Врага'''
class Enemy1_1(GameSprite):
    def update(self):
        if self.rect.y <= 320 or self.rect.y >= 740:
            self.speed *= -1
        self.rect.y += self.speed

class Enemy5_1(GameSprite):
    def update(self):
        if self.rect.x <= 200 or self.rect.x >= 340:
            self.speed *= -1
        self.rect.x += self.speed

class Enemy5_2(GameSprite):
    def update(self):
        if self.rect.y <= 300 or self.rect.y >= 440:
            self.speed *= -1
        self.rect.y += self.speed

class Enemy5_3(GameSprite):
    def update(self):
        if self.rect.x <= 810 or self.rect.x >= 940:
            self.speed *= -1
        self.rect.x += self.speed

class Enemy5_4(GameSprite):
    def update(self):
        if self.rect.x <= 720 or self.rect.x >= 1020:
            self.speed *= -1
        self.rect.x += self.speed

'''Класс для Стен'''
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((wall_width, wall_height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = self.wall_x
        self.rect.y = self.wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Button(sprite.Sprite):
    def __init__(self, ref_image, pos_x, pos_y, size_x, size_y):
        self.image = transform.scale( image.load(ref_image), (size_x, size_y) )
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def click(self, function):
        pressed = mouse.get_pressed()
        pos = mouse.get_pos()
        if pressed[0]:
            if self.rect.collidepoint(pos):
                function()
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
win_width = 1100
win_height = 810
window = display.set_mode( (win_width, win_height) )
display.set_caption('Лабиринт')
back = transform.scale( image.load('background.jpg'), (win_width, win_height) )

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

background = transform.scale(image.load('background.jpg'), (1100, 810))
nastroykyV = transform.scale(image.load('background.jpg'), (600, 400))

game = True
finish = False
menu = True
level = False
lvl1 = False
lvl2 = False
lvl3 = False
lvl4 = False
lvl5 = False
g = True
FPS = 30
clock = time.Clock()

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (255, 215, 15))
lose = font.render("YOU LOSE!", True, (255, 0, 0))

player = Player('hero.png', 5, win_height - 80, 4)
player1 = Player('hero.png', 5, win_height - 80, 4)
monster1_1 = Enemy1_1('cyborg.png', 850, 350, 20)
monster5_1 = Enemy5_1('cyborg.png', 330, 320, 2)
monster5_2 = Enemy5_2('cyborg.png', 130, 420, 2)
monster5_3 = Enemy5_3('cyborg.png', 831, 100, 2)
monster5_4_1 = Enemy5_4('cyborg.png', 750, 450, 3)
monster5_4_2 = Enemy5_4('cyborg.png', 825, 550, 3)
monster5_4_3 = Enemy5_4('cyborg.png', 900, 650, 3)
monster5_4_4 = Enemy5_4('cyborg.png', 975, 750, 3)
final = GameSprite('treasure.png', win_width - 120,win_height - 100, 0)
button_play = Button('play.png', 450, 350, 200, 100)
button_1 = Button('1.png', 100, 50, 100, 100)
button_2 = Button('2.png', 300, 50, 100, 100)
button_3 = Button('3.png', 500, 50, 100, 100)
button_4 = Button('4.png', 700, 50, 100, 100)
button_5 = Button('5.png', 900, 50, 100, 100)
button_nas = Button('nastroyky.png', 0, 0, 100, 100)
button_str1 = Button('1.png', 0, 350, 50, 50)

def click_playstr1():
    global menu
    global level
    menu = True
    level = False

def click_play():
    global menu
    global level
    menu = False
    level = True

def click_play1():
    global level
    global lvl1
    level = False
    lvl1 = True

def click_play2():
    global level
    global lvl2
    level = False
    lvl2 = True

def click_play3():
    global level
    global lvl3
    level = False
    lvl3 = True

def click_play4():
    global level
    global lvl4
    level = False
    lvl4 = True

def click_play5():
    global level
    global lvl5
    level = False
    lvl5 = True

def click_playN():
    global nast


'''Расположение стен'''
wG1 = Wall(255, 0, 0, 0, 0, 1, 810)
wG2 = Wall(255, 0, 0, 0, 0, 1200, 1)
wG3 = Wall(255, 0, 0, 1200, 0, 1, 810)
wG4 = Wall(255, 0, 0, 0, 810, 1200, 1)
wl1 = Wall(0, green, blue, 400, 400, 10, 100)
w1_w1 = Wall(0, 0, 255, 100, 800, 510, 10)
w1_w2 = Wall(0, 0, 255, 100, 0, 10, 600)
w1_w3 = Wall(0, 0, 255, 300, 200, 10, 600)
w1_w4 = Wall(0, 0, 255, 400, 0, 10, 600)
w1_w5 = Wall(0, 0, 255, 600, 100, 10, 700)
w1_w6 = Wall(0, 0, 255, 600, 100, 400, 10)
w1_w7 = Wall(0, 0, 255, 700, 300, 400, 10)
w1_w8 = Wall(0, 0, 255, 700, 300, 10, 400)

w2_w1 = Wall(0, 0, 255, 100, 800, 500, 10)
#w2_w2 = Wall()
w3_w1 = Wall(0, 0, 255, 100, 800, 500, 10)
#w3_w2 = Wall()
w4_w1 = Wall(0, 0, 255, 100, 800, 500, 10)
#w4_w2 = Wall()
w5_w1 = Wall(0, 0, 255, 100, 0, 600, 10)
w5_w2 = Wall(0, 0, 255, 100, 0, 10, 300)
w5_w3 = Wall(0, 0, 255, 200, 100, 10, 300)
w5_w4 = Wall(0, 0, 255, 200, 100, 100, 10)
w5_w5 = Wall(0, 0, 255, 300, 200, 100, 10)
w5_w6 = Wall(0, 0, 255, 400, 0, 10, 300)
w5_w7 = Wall(0, 0, 255, 100, 400, 600, 10)
w5_w8 = Wall(0, 0, 255, 500, 100, 10, 300)
w5_w9 = Wall(0, 0, 255, 500, 100, 100, 10)
w5_w10 = Wall(0, 0, 255, 200, 300, 100, 10)
w5_w11 = Wall(0, 0, 255, 600, 200, 100, 10)
w5_w12 = Wall(0, 0, 255, 500, 300, 100, 10)
w5_w13 = Wall(0, 0, 255, 100, 800, 600, 10)
w5_w14 = Wall(0, 0, 255, 100, 500, 10, 200)
w5_w15 = Wall(0, 0, 255, 100, 700, 200, 10)
w5_w16 = Wall(0, 0, 255, 400, 600, 10, 200)
w5_w17 = Wall(0, 0, 255, 0, 500, 600, 10)
w5_w18 = Wall(0, 0, 255, 0, 290, 100, 10)
w5_w19 = Wall(0, 0, 255, 200, 600, 200, 10)
w5_w20 = Wall(0, 0, 255, 500, 500, 10, 200)
w5_w21 = Wall(0, 0, 255, 500, 700, 100, 10)
w5_w22 = Wall(0, 0, 255, 700, 400, 10, 410)
w5_w23 = Wall(0, 0, 255, 600, 600, 100, 10)
w5_w24 = Wall(0, 0, 255, 700, 0, 10, 300)
w5_w25 = Wall(0, 0, 255, 800, 300, 210, 10)
w5_w26 = Wall(0, 0, 255, 800, 100, 10, 200)
w5_w27 = Wall(0, 0, 255, 900, 0, 10, 200)
w5_w28 = Wall(0, 0, 255, 1000, 100, 10, 200)
w5_w29 = Wall(0, 0, 255, 800, 300, 10, 110)
w5_w30 = Wall(0, 0, 255, 700, 400, 100, 10)
w5_w31 = Wall(0, 0, 255, 900, 400, 200, 10)

timer = 0
new_color = '1'
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if lvl1 == True:
        if not finish:
            window.blit(back, (0, 0) )
            w1_w1.draw_wall()
            w1_w2.draw_wall()
            w1_w3.draw_wall()
            w1_w4.draw_wall()
            w1_w5.draw_wall()
            w1_w6.draw_wall()
            w1_w7.draw_wall()
            w1_w8.draw_wall()
            monster1_1.update()
            monster1_1.reset()
            player1.update()
            player1.reset()
            final.reset()
            button_nas.reset()
            button_nas.click(click_playN)
        if sprite.collide_rect(player1, monster1_1) or sprite.collide_rect(player1, wG1) or sprite.collide_rect(player1, wG2) or sprite.collide_rect(player1, wG3) or sprite.collide_rect(player1, wG4) or sprite.collide_rect(player1, w1_w1) or sprite.collide_rect(player1, w1_w2) or sprite.collide_rect(player1, w1_w3) or sprite.collide_rect(player1, w1_w4) or sprite.collide_rect(player1, w1_w5) or sprite.collide_rect(player1, w1_w6) or sprite.collide_rect(player1, w1_w7) or sprite.collide_rect(player1, w1_w8):
            print(live - nbv)
            player1 = Player('hero.png', 5, win_height - 80, 4)
            nbv = nbv + 1
            if nbv == live:
                finish = True
                window.blit(lose, (440, 400))
                kick.play()
            else:
                player1.reset()
        if sprite.collide_rect(player1, final):
            finish = True
            window.blit(win, (440, 400))
            money.play()
    elif lvl2 == True:
        if not finish:
            window.blit(back, (0, 0) )
            w2_w1.draw_wall()
            player.update()
            monster1.update()
            monster2.update()
            player.reset()
            monster1.reset()
            monster2.reset()
            final.reset()
            button_nas.reset()
            button_nas.click(click_playN)
        if sprite.collide_rect(player, monster1) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, wG1) or sprite.collide_rect(player, wG2) or sprite.collide_rect(player, wG3) or sprite.collide_rect(player, wG4) or sprite.collide_rect(player, w2_w1):
            nbv = nbv + 1
            print(live - nbv)
            player = Player('hero.png', 5, win_height - 80, 4)
            if nbv == live:
                finish = True
                window.blit(lose, (440, 400))
                kick.play()
            else:
                player.reset()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (440, 400))
            money.play()
    elif lvl3 == True:
        if not finish:
            window.blit(back, (0, 0) )
            player.update()
            monster1.update()
            monster2.update()
            player.reset()
            monster1.reset()
            monster2.reset()
            final.reset()
            button_nas.reset()
            button_nas.click(click_playN)
        if sprite.collide_rect(player, monster1) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, wG1) or sprite.collide_rect(player, wG2) or sprite.collide_rect(player, wG3) or sprite.collide_rect(player, wG4) or sprite.collide_rect(player, w3_w1):
            nbv = nbv + 1
            print(live - nbv)
            player = Player('hero.png', 5, win_height - 80, 4)
            if nbv == live:
                finish = True
                window.blit(lose, (440, 400))
                kick.play()
            else:
                player.reset()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (440, 400))
            money.play()
    elif lvl4 == True:
        if not finish:
            window.blit(back, (0, 0) )
            player.update()
            monster1.update()
            monster2.update()
            player.reset()
            monster1.reset()
            monster2.reset()
            final.reset()
            button_nas.reset()
            button_nas.click(click_playN)
        if sprite.collide_rect(player, monster1) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, wG1) or sprite.collide_rect(player, wG2) or sprite.collide_rect(player, wG3) or sprite.collide_rect(player, wG4) or sprite.collide_rect(player, w4_w1):
            nbv = nbv + 1
            print(live - nbv)
            player = Player('hero.png', 5, win_height - 80, 4)
            if nbv == live:
                finish = True
                window.blit(lose, (440, 400))
                kick.play()
            else:
                player.reset()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (440, 400))
            money.play()
    elif lvl5 == True:
        timer += 1
        if timer >= walll1:
            if blue == 255 and green == 0:
                blue = 0
                green = 255
                timer = 0
                wl1 = Wall(0, green, blue, 400, 400, 10, 100)
                walll1 = random.randint(30,90)
            elif blue == 0 and green == 255:
                blue = 255
                green = 0
                timer = 0
                wl1 = Wall(0, green, blue, 400, 400, 10, 100)
                walll1 = random.randint(30,90)
        if not finish:
            window.blit(back, (0, 0) )
            w5_w1.draw_wall()
            w5_w2.draw_wall()
            w5_w3.draw_wall()
            w5_w4.draw_wall()
            w5_w5.draw_wall()
            w5_w6.draw_wall()
            w5_w7.draw_wall()
            w5_w8.draw_wall()
            w5_w9.draw_wall()
            w5_w10.draw_wall()
            w5_w11.draw_wall()
            w5_w12.draw_wall()
            w5_w13.draw_wall()
            w5_w14.draw_wall()
            w5_w15.draw_wall()
            w5_w16.draw_wall()
            w5_w17.draw_wall()
            w5_w18.draw_wall()
            w5_w19.draw_wall()
            w5_w20.draw_wall()
            w5_w21.draw_wall()
            w5_w22.draw_wall()
            w5_w23.draw_wall()
            w5_w24.draw_wall()
            w5_w25.draw_wall()
            w5_w26.draw_wall()
            w5_w27.draw_wall()
            w5_w28.draw_wall()
            w5_w29.draw_wall()
            w5_w30.draw_wall()
            w5_w31.draw_wall()
            wG1.draw_wall()
            wG2.draw_wall()
            wG3.draw_wall()
            wG4.draw_wall()
            wl1.draw_wall()
            player1.update()
            monster5_1.update()
            monster5_2.update()
            monster5_3.update()
            monster5_4_1.update()
            monster5_4_2.update()
            monster5_4_3.update()
            monster5_4_4.update()
            player1.reset()
            monster5_1.reset()
            monster5_2.reset()
            monster5_3.reset()
            monster5_4_1.reset()
            monster5_4_2.reset()
            monster5_4_3.reset()
            monster5_4_4.reset()
            final.reset()
            button_nas.reset()
            button_nas.click(click_playN)
        if sprite.collide_rect(player1, monster5_1) or sprite.collide_rect(player1, monster5_2) or sprite.collide_rect(player1, monster5_3) or sprite.collide_rect(player1, monster5_4_1) or sprite.collide_rect(player1, monster5_4_2) or sprite.collide_rect(player1, monster5_4_3) or sprite.collide_rect(player1, monster5_4_4) or sprite.collide_rect(player1, w5_w1) or sprite.collide_rect(player1, w5_w2) or sprite.collide_rect(player1, w5_w3) or sprite.collide_rect(player1, w5_w4) or sprite.collide_rect(player1, w5_w5) or sprite.collide_rect(player1, w5_w6) or sprite.collide_rect(player1, w5_w7) or sprite.collide_rect(player1, w5_w8) or sprite.collide_rect(player1, w5_w9) or sprite.collide_rect(player1, w5_w10) or sprite.collide_rect(player1, w5_w11) or sprite.collide_rect(player1, w5_w12) or sprite.collide_rect(player1, w5_w13) or sprite.collide_rect(player1, w5_w14) or sprite.collide_rect(player1, w5_w15) or sprite.collide_rect(player1, w5_w16) or sprite.collide_rect(player1, w5_w17) or sprite.collide_rect(player1, w5_w18) or sprite.collide_rect(player1, w5_w19) or sprite.collide_rect(player1, w5_w20) or sprite.collide_rect(player1, w5_w21) or sprite.collide_rect(player1, w5_w22) or sprite.collide_rect(player1, w5_w23) or sprite.collide_rect(player1, w5_w24) or sprite.collide_rect(player1, w5_w25) or sprite.collide_rect(player1, w5_w26) or sprite.collide_rect(player1, w5_w27) or sprite.collide_rect(player1, w5_w28) or sprite.collide_rect(player1, w5_w29) or sprite.collide_rect(player1, w5_w30) or sprite.collide_rect(player1, w5_w31) or sprite.collide_rect(player1, wG1) or sprite.collide_rect(player1, wG2) or sprite.collide_rect(player1, wG3) or sprite.collide_rect(player1, wG4):
            nbv = nbv + 1
            print(live - nbv)
            player1 = Player('hero.png', 5, win_height - 80, 4)
            player1.reset()
        if nbv == live:
            finish = True
            window.blit(lose, (480, 400))
            kick.play()
        if blue == 255:
            if sprite.collide_rect(player1, wl1):
                nbv = nbv + 1
                print(live - nbv)
                player = Player('hero.png', 5, win_height - 80, 4)
        if sprite.collide_rect(player1, final):
            finish = True
            window.blit(win, (480, 400))
            money.play()
    elif menu:
        window.blit(background, (0, 0))
        button_play.reset()
        button_play.click(click_play)
        button_nas.reset()
        button_nas.click(click_playN)
    elif level:
        window.blit(background, (0, 0))
        button_1.reset()
        button_1.click(click_play1)
        button_2.reset()
        button_2.click(click_play2)
        button_3.reset()
        button_3.click(click_play3)
        button_4.reset()
        button_4.click(click_play4)
        button_5.reset()
        button_5.click(click_play5)
        button_str1.reset()
        button_str1.click(click_playstr1)
    elif nast:
        window.blit(nastroykyV, (300, 200))
    display.update()
    clock.tick(FPS)
