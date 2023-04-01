from pygame import *
from datetime import datetime, timedelta
from random import randint
win_width = 1400

win_height = 600
display.set_caption("Flappy Birds")
window = display.set_mode((win_width, win_height))

run = True
finish = False
clock = time.Clock()
FPS = 60

background = transform.scale(
    image.load("ground.png"),
    (win_width, win_height)
)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.next_jump = datetime.now()

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, wight, height)
        self.speed = player_speed
    def update(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and self.rect.y > 80:
            if self.next_jump <= datetime.now():                         
                self.rect.y -= 100
                self.next_jump = datetime.now() + timedelta(seconds = 0.2)
            
        self.rect.y += self.speed *2

class Obstacles(GameSprite):
    def update(self):
        self.rect.x += self.speed




bird = Player('bird1.jpg', 200, 200, 2, 50, 50)
tryba = Obstacles("tryba1.jpg", 1200, 400, 200, 200)
tryban2 = Obstacles("tryba2.jpg", 1200, 0, 200, 200)

font.init()
score_text = font.SysFont("Arial", 20)
point_x = 0
lost_text = font.SysFont('Arial', 20)
point_y = 0



while run:
    window.blit(background, (0, 0))

    xy = score_text.render(str(point_x), 1, (0,0,0))
    window.blit(xy, (10, 20))


    for e in event.get():
        if e.type == QUIT:
           run = False
   
    


    if finish == False:
        bird.reset()
        tryba.reset()
        tryban2.reset()
        bird.update()
        
        if sprite.collide_rect(tryba, bird) or sprite.collide_rect(tryban2, bird) :
            finish = True
            




    display.update()
    clock.tick(FPS)
