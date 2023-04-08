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
        self.rect.x -= self.player.speed



bird = Player('bird1.png', 200, 200, 2, 50, 50)
tryba = Obstacles("tryba1.png", 1200, randint(200, win_width - 800), 200, 200, bird)
tryban2 = Obstacles("tryba2.png", 1200,  randint(0, win_width + 40), 200, 200, bird)

font.init()
score_text = font.SysFont("Arial", 20)
point_x = 0
lost_text = font.SysFont('Arial', 20)
point_y = 0

ground_scroll = 0
scroll_speed = 4

while run:
    window.blit(background, (0, 0))

    xy = score_text.render(str(point_x), 1, (0,0,0))
    window.blit(xy, (10, 20))


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
        
        if sprite.collide_rect(tryba, bird) or sprite.collide_rect(tryban2, bird) or bird.rect.x >= 400:
            finish = True
            




    display.update()
    clock.tick(FPS)
