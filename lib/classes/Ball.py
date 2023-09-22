from lib.utils.initials import *
import random


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity_x = 0.7
        self.velocity_y = 0.7

    def draw(self):
        pygame.draw.circle(wn, BLUE, (self.x, self.y), radius)

    def move(self):
        # ball move logic
        self.x += self.velocity_x
        self.y += self.velocity_y

    def check_collisions(self, left_paddle, right_paddle):
        # ball collision handling
        if self.y <= 0 + self.radius or self.y >= HEIGHT - self.radius:
            self.velocity_y *= -1
        if left_paddle.x_pos <= self.x <= left_paddle.x_pos + paddle_width:
            if left_paddle.y_pos <= self.y <= left_paddle.y_pos + paddle_height:
                self.velocity_x *= -1

        if right_paddle.x_pos <= self.x <= right_paddle.x_pos + paddle_width:
            if right_paddle.y_pos <= self.y <= right_paddle.y_pos + paddle_height:
                self.velocity_x *= -1

    def reset(self):
        # ball position reset
        if self.x >= WIDTH - self.radius:
            # player1_score += 1
            self.x, self.y = WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius
            # randomize velocity and angle
            self.angle_velocity_randomize(self)
        if self.x <= 0 + self.radius:
            # player2_score += 1
            self.x, self.y = WIDTH / 2 - self.radius, HEIGHT / 2 - self.radius
            self.angle_velocity_randomize(self)

    @staticmethod
    def angle_velocity_randomize(self):
        direction = random.choice(direction_choose)
        ang = random.choice(angle_choose)
        if direction == 0:
            if ang == 0:
                self.velocity_y, self.velocity_x = -0.9, 0.80
            if ang == 1:
                self.velocity_y, self.velocity_x = -0.80, 0.80
            if ang == 2:
                self.velocity_y, self.velocity_x = -0.80, 0.9
        if direction == 1:
            if ang == 0:
                self.velocity_y, self.velocity_x = 0.9, 0.80
            if ang == 1:
                self.velocity_y, self.velocity_x = 0.80, 0.80
            if ang == 2:
                self.velocity_y, self.velocity_x = 0.80, 0.9
