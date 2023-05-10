from pygame import *
from random import randint
import time as time1 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=70, height=70):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed   

window = display.set_mode((700,500))
display.set_caption("Ping Pong")
window.fill((130,100,200))

rocket1 = Player('Rocket.png', 25,150,3,15,50)
rocket2 = Player('Rocket2.png', 650,150,3,15,50)
ball = GameSprite('basketball.png', 250,150,3,15,50)

clock = time.Clock()
FPS = 60
finish = False
game = True
speed_x = 3
speed_y = 3
font.init()
l1 = font.Font(None, 24,)
lose1 = l1.render('player1 lose',True,(255,0,0 ))
lose2 = l1.render('player2 lose',True,(255,0,0 ))
while game:

    



    for e in event.get():
        if e.type == QUIT:
            game = False   


    if finish != True:

        window.fill((130,100,200))
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
        rocket1.update_l()
        rocket2.update_r()
        rocket1.reset()
        rocket2.reset()
        ball.update()
        ball.reset()
    
    if ball.rect.y >= 450 or ball.rect.y == 0:
        speed_y *= -1

    if ball.rect.x <= 0:
        finish = True
        window.blit(lose1,(200,200))    
    if ball.rect.x >= 650:
        finish = True
        window.blit(lose2,(200,200))        
    
        


    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2,ball):
        speed_x *= -1


    clock.tick(60)
    display.update()