import pygame as pg

class Player:

    def __init__(self, screen):
        self.angle = 0
        self.next_angle = 0
        self.win = screen 
        self.x = 300
        self.y = 300
        self.sur = pg.image.load('tank.png')
        self.sur = pg.transform.scale(self.sur,
                                      (self.sur.get_width() /8, self.sur.get_height() /8))

    def move(self, keys):
        if keys[pg.K_w]:
            self.y -= 5
            self.angle = 0
        elif keys[pg.K_s]:
            self.y += 5
            self.angle = 180
        elif keys[pg.K_a]:
            self.x -= 5
            self.angle = 270
        elif keys[pg.K_d]:
            self.x += 5
            self.angle = 90
            self.next_angle = self.angle
        self.sur = pg.transform.rotate(self.sur, self.next_angle)

        
    def draw(self):
        rect = self.sur.get_rect(center=(self.x, self.y))
        self.win.blit(self.sur, rect)

    def update(self):
        pass