from pygame import *
from time import time as timer

BACK = (200,255,255)
img_ball = 'ball.png'
img_racket = 'platform.png' 
FPS = 60
win_width = 900
win_height = 700
speed_x = 3
speed_y = 3

font.init()
font_goal = font.SysFont('Arial', 40)
font_time = font.SysFont('Arial', 28)
lose_right = font_goal.render('PLAYER LEFT WIN!', True, (180, 0, 0))
lose_left = font_goal.render('PLAYER RIGHT WIN!', True, (180, 0, 0))
goal_right = 0
goal_left = 0



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

    def colliderect(self, block):
        return sprite.collide_rect(self, block)
        



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
            

ball = Gamesprite(img_ball, 425, 325, 50, 50, 4)
racket_1 = Right(img_racket, 860, 300, 30, 100, 4)
racket_2 = Left(img_racket, 10, 300, 30, 100, 4)


game = True
finish = False
start_time = timer()
while game:
    current_time = timer()
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(BACK)
        racket_1.update()
        racket_2.update()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 640 or ball.rect.y < 10:
            speed_y *= -1

        if ball.colliderect(racket_1) or ball.colliderect(racket_2):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.x < 10:
            goal_right += 15
            ball.rect.x = 425
            ball.rect.y = 325
            time.delay(500)

        if ball.rect.x > 840:
            goal_right += 15
            ball.rect.x = 425
            ball.rect.y= 325
            time.delay(500)


        check_left = font_time.render(str(goal_right), True, (0,0,0))
        check_right = font_time.render(str(goal_left), True, (0,0,0))
        check_DOT = font_time.render(' - ', True, (0,0,0))
        window.blit(check_left, (410, 25))
        window.blit(check_DOT, (445, 25))
        window.blit(check_right, (485, 25))



        if goal_right > 45:
            window.blit(lose_left, (200, 300))

        if goal_right > 45:
            window.blit(lose_left, (200, 300))
            finish = True

        racket_1.reset()
        racket_2.reset()
        ball.reset()

        if current_time - start_time >= 30:
            start_time = timer
            speed_x += 1
            speed_y += 1

    else:
        start_time = timer()
        time.delay(3000)
        ball.rect.x = 425
        ball.rect.y = 325
        racket_1.rect.y = 300
        racket_2.rect.y = 300
        goal_left = 0
        goal_right = 0
        finish = False




    display.update()
    clock.tick(FPS)