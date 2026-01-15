from pygame import *
from time import sleep
window = display.set_mode((600,400))
bg= transform.scale(image.load("sky.jpg"),(700,500))
display.set_caption("Ping-Pong")
fps = time.Clock()

font.init()
font3 = font.SysFont("Impact",74)

class Gamespite(sprite.Sprite):
    def __init__(self,img,x,y,speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(img),(width,height))
        self.x = x 
        self.y = y
        self.direction = "left"
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.width = width

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player1(Gamespite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y >= 5: 
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 400-65:
            self.rect.y += self.speed

class Player2(Gamespite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >= 5: 
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y <= 400-65:
            self.rect.y += self.speed

class Ball(Gamespite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
            
    def collide (self,rect):
        return self.rect.colliderect(rect)

player1 = Player1("racket 1.png", 500, 150, 10, 100, 100)
player2 = Player2("racket 2.png", 0, 150 , 10, 100 ,100)
ball = Ball("ball.png", 300, 200, 1, 50,50)

speed_x = 5
speed_y = 5
finish = False

game = True
while game is True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 400 - 50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1

    if ball.rect.x > 600-50: #player 1 lose
        win = font3.render("Player 2 win",True,(0,255,0))
        window.blit(win,(125,150))
        display.update()
        sleep(1)
        game = False

    if ball.rect.x < 0: #player 2 lose
        win = font3.render("Player 1 win",True,(0,255,0))
        window.blit(win,(125,150))
        display.update()
        sleep(1)
        game = False

    window.blit(bg,(0,0))
    ball.reset()
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()

    fps.tick(60)
    display.update()

