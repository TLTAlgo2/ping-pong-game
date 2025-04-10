 
from pygame import *
from random import randint
from time import time as tm 

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

 def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullets.add(Bullet('bullet.png', self.rect.centerx, self.rect.centery, 20, 20, 20 ))
    
        bullet = mixer.music.load('fire.ogg')

width = 500
height = 500

window = display.set_mode((width, height)) 
window.fill((0, 0, 0))
clock = time.Clock()
FPS = 60

player_one.

start = True
while start == True:
    for e in event.get():
        if e.type == QUIT:
            start = False
    display.update()
    clock.tick(FPS)