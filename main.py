from pygame import *
from datetime import datetime, timedelta
from random import randint
win_width = 1200

win_height = 700
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
        if keys[K_SPACE] and self.rect.y > 50:
            if self.next_jump <= datetime.now():                         
                self.rect.y -= 100
                self.next_jump = datetime.now() + timedelta(seconds = 0.45)
            
        self.rect.y += self.speed *1.4

class Obstacles(GameSprite):
    def __init__(self, player_image, player_x, player_y, wight, height, player):
        super().__init__(player_image, player_x, player_y, wight, height)
        self.player = player

    def update(self):
        self.rect.x -= 3



bird = Player('bird1.png', 200, 200, 2, 50, 50)
tryba = Obstacles("tryba1.png", 1200, 453, 200, 200, bird)
tryban2 = Obstacles("tryba2.png", 1200, 0, 200, 200, bird)
tryban3 = Obstacles("tryba1.png", 2000, 453, 200, 200, bird)
tryban4 = Obstacles("tryba2.png", 2000, 0, 200, 200, bird)
trigger_point = Obstacles("block.png", 1360, 230, 100, 200, bird)
trigger_point2 = Obstacles("block.png", 2160, 230, 100, 200, bird)



font.init()
score_text = font.SysFont("Arial", 50)
point_x = 0
lost_text = font.SysFont('Arial', 100)


while run:
    window.blit(background, (0, 0))

    xy = score_text.render(str(point_x), 1, (0,0,0))
    window.blit(xy, (550, 25))


    for e in event.get():
        if e.type == QUIT:
           run = False
   
    
    

    if finish == False:
        bird.reset()
        bird.update()

        tryba.reset()
        tryba.update()

        tryban2.reset()
        tryban2.update()

        tryban3.reset()
        tryban3.update()

        tryban4.reset()
        tryban4.update()

        trigger_point.update()

        trigger_point2.update()


        if tryba.rect.x < 0:
            tryba.rect.x += 1800 
        if tryban2.rect.x < 0:
            tryban2.rect.x += 1800   #1 труба
        if tryban3.rect.x < 0:
            tryban3.rect.x += 1800
        if tryban4.rect.x < 0:
            tryban4.rect.x += 1800 #2 труба 
        if trigger_point.rect.x < 0:
            trigger_point.rect.x += 1800
        if trigger_point2.rect.x < 0:
            trigger_point2.rect.x += 1800 


        if sprite.collide_rect(bird, trigger_point) or sprite.collide_rect(bird, trigger_point2):
            point_x += 0.021
    if sprite.collide_rect(tryba, bird) or sprite.collide_rect(tryban2, bird) or sprite.collide_rect(tryban3, bird) or sprite.collide_rect(tryban4, bird) or bird.rect.y >= 600:
        finish = True
        text5 = lost_text.render("Ви програли", 1, (0, 0, 0))
        window.blit(text5, (350, 250))
            
    if score_text == 25:
        finish = True



    display.update()
    clock.tick(FPS)
