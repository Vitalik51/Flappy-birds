from pygame import *
from datetime import datetime, timedelta
  
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
        if keys[K_SPACE] and self.rect.y > 5:
            if self.next_jump <= datetime.now():                         
                self.rect.y -= 100
                self.next_jump = datetime.now() + timedelta(seconds = 0.3)  
        self.rect.x += self.speed
        self.rect.y += self.speed *2
        
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
 
run = True
finish = False
clock = time.Clock()
FPS = 60


bird = Player('bird.png', 200, 200, 2, 50, 50)
tryba = GameSprite('tryba.png', 400, 400, 50, 80)

font.init()
score_text = font.SysFont("Arial", 20)
point_x = 0
lost_text = font.SysFont('Arial', 20)
point_y = 0



while run:
    window.fill(back)

    xy = score_text.render(str(point_x), 1, (0,0,0))
    window.blit(xy, (10, 20))


    for e in event.get():
        if e.type == QUIT:
           run = False
   
    


    if finish == False:
        bird.reset()
        tryba.reset()
        bird.update()
        if sprite.collide_rect(tryba, bird):
            finish = True





    display.update()
    clock.tick(FPS)
