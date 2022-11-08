import pygame as pg
import pygame.time as time
import sys
from random import randint
import tkinter.messagebox as tkm


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) 
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg)
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -5],
        pg.K_DOWN:  [0, +5],
        pg.K_LEFT:  [-5, 0],
        pg.K_RIGHT: [+5, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Food:
    def __init__(self, color, radius, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate



def main():
    score = 0
    #背景
    scr = Screen("食え！！こうかとん", (1600, 900), "ex06/fig/pg_bg.jpg")

    #こうかとん
    kkt = Bird("ex06/fig/2.png", 2.0, (900, 400))

    #爆弾
    bkd0 = Bomb((255, 0, 0), 10, (+1.5, +1.5), scr)
    bkd1 = Bomb((255, 0, 0), 10, (+1.5, +1.5), scr)
    bkd2 = Bomb((255, 0, 0), 10, (+1.5, +1.5), scr)
    bkd3 = Bomb((255, 0, 0), 10, (+1.5, +1.5), scr)

    #餌
    esa = Food((255,255,0),10, scr)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        #こうかとん
        kkt.update(scr)

        #爆弾
        bkd0.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)

        esa.blit(scr)       

        if kkt.rct.colliderect(esa.rct):#餌get時
            score += 1
            esa = Food((255,255,0),10, scr)

        #勝利処理
        if score >= 10:
            return tkm.showinfo("YUO WIN","おめでとう")
        
        #敗北処理
        if (kkt.rct.colliderect(bkd0.rct) or 
            kkt.rct.colliderect(bkd1.rct) or 
            kkt.rct.colliderect(bkd2.rct) or 
            kkt.rct.colliderect(bkd3.rct) or
            time.get_ticks() >= 60000):
            return tkm.showinfo("YUO DIE","あ～あ")

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()