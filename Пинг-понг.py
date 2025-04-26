from pygame import *
from time import time as timer

BACK = (200,255,255)
img_ball = 'ball.png'
img_racket = 'platform.png' 
FPS = 60
win_width = 900
win_height = 700
speed_x = 0.707
speed_y = 0.707

front.init()
font_goal = font.SysFont('Arial', 40)
font_time = font.SysFont('Arial', 28)

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')
window.fill(BACK)
clock = time.Clock()

class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = image.load(img)
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Right(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
            
class Left(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
            

class Ball(Gamesprite):
    def update(self):
        self.rect.x = self.rect.x + self.speed * speed_x
        self.rect.y = self.rect.y + self.speed * speed_y

        if self.rect.y > win_height or self.rect.y < 0:
            speed_y *= -1

        