from lib.utils.initials import *

class Paddle:
    def __init__(self, x, y):
        self.w = paddle_width
        self.h = paddle_height
        self.col = RED
        self.x_pos = x
        self.y_pos = y
        self.vel = 0

    def draw(self):
        pygame.draw.rect(wn, self.col, pygame.Rect(self.x_pos, self.y_pos, self.w, self.h))


    def collisions(self):
        if self.y_pos >= HEIGHT - paddle_height:
            self.y_pos = HEIGHT - paddle_height
        if self.y_pos <= 0:
            self.y_pos = 0

