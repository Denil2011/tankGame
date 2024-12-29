import pygame as pg
from player_tank import Player

class Game:

    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((600, 600))
        self.player = Player(self.win)
        self.clock = pg.time.Clock()

    def game(self):
        while True:
            self.move()
            self.draw()
            self.update()


    def move(self):
        for event in pg.event.get():
             if event.type == pg.QUIT:
                  pg.quit()
            self.player.move(pg.key.get_pressed())

    def draw(self):
        self.win.fill('white')
        self.player.draw()

    def update(self):
        self.clock.tick(60)
        pg.display.update()

Game().game()