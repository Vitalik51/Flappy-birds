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
        self.original_y = player_y
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
                self.next_jump = datetime.now() + timedelta(seconds = 0.40)
            
        self.rect.y += self.speed *1.4

class Obstacles(GameSprite):
    def __init__(self, player_image, player_x, player_y, wight, height, player):
        super().__init__(player_image, player_x, player_y, wight, height)
        self.player = player

    def update(self):
        self.rect.x -= 4
        if point_x >= 1:
            self.rect.x -= 1
        if point_x >= 2:
            self.rect.x -= 1
        if point_x >= 3:
            self.rect.x -= 1
        if point_x >= 4:
            self.rect.x -= 1
        if point_x >= 5:
            self.rect.x +=4
        if point_x >= 6:
            self.rect.x -= 1
        if point_x >= 7:
            self.rect.x -= 1
        if point_x >= 8:
            self.rect.x -= 1
        if point_x >= 9:
            self.rect.x -= 1
        if point_x >= 10:
            self.rect.x += 5 
        if point_x >= 11:
            self.rect.x -= 1
        if point_x >= 12:
            self.rect.x -= 1
        if point_x >= 13:
            self.rect.x -= 1
        if point_x >= 14:
            self.rect.x -= 1
        if point_x >= 15:
            self.rect.x += 4
        if point_x >= 16:
            self.rect.x -= 1
        if point_x >= 17:
            self.rect.x -= 1
        if point_x >= 18:
            self.rect.x -= 1
        if point_x >= 19:
            self.rect.x -= 1
        if point_x >= 20:
            self.rect.x += 1
        if point_x >= 21:
            self.rect.x -= 1
        if point_x >= 22:
            self.rect.x -= 1 
        if point_x >= 23:
            self.rect.x -= 1
        if point_x >= 24:
            self.rect.x += 5 


bird = Player('bird1.png', 200, 200, 2, 50, 50)
tryba = Obstacles("tryba1.png", 1200, 453, 200, 200, bird)
tryban2 = Obstacles("tryba2.png", 1200, -50, 200, 200, bird)
tryban3 = Obstacles("tryba1.png", 2000, 453, 200, 200, bird)
tryban4 = Obstacles("tryba2.png", 2000, -50, 200, 200, bird)

trybu = [
    tryba,
    tryban2,
    tryban3,
    tryban4
]
trigger_point = Obstacles("block.png", 1360, 230, 100, 200, bird)
trigger_point2 = Obstacles("block.png", 2160, 230, 100, 200, bird)



font.init()
score_text = font.SysFont("Arial", 50)
point_x = 0
lost_text = font.SysFont('Arial', 100)
win_text = font.SysFont('Arial', 100)


while run:
    


    for e in event.get():
        if e.type == QUIT:
           run = False
   
    
    

    if finish == False:

        window.blit(background, (0, 0))

        bird.update()

        trigger_point.update()
        trigger_point2.update()

        for t in trybu:
            t.update()
            if t.rect.x < 0:
                t.rect.x += 1500
                t.rect.y = t.original_y + randint (-50,  50)




        if sprite.collide_rect(bird, trigger_point):
            point_x += 1
            trigger_point.rect.x += 1500
        if sprite.collide_rect(bird, trigger_point2):
            point_x += 1
            trigger_point2.rect.x += 1500 

        bird.reset()

        for t in trybu:
            t.reset()

        xy = score_text.render(str(point_x), 1, (0,0,0))
        window.blit(xy, (550, 25))

    if sprite.collide_rect(tryba, bird) or sprite.collide_rect(tryban2, bird) or sprite.collide_rect(tryban3, bird) or sprite.collide_rect(tryban4, bird) or bird.rect.y >= 600:
        finish = True
        text5 = lost_text.render("Ви програли", 1, (0, 0, 0))
        window.blit(text5, (350, 250))
            
    if point_x == 25:
        finish = True
        text6 = win_text.render("Ви виграли", 1, (0, 0, 0))
        window.blit(text6, (350, 250))


    display.update()
    clock.tick(FPS)
