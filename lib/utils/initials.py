import pygame

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
run = True
direction = [0, 1]
angle = [0, 1, 2]
player1_score = player2_score = 0

pygame.init()

# COLORS
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# for the ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
ball_vel_x, ball_vel_y = 0.2, 0.2

# for the paddles
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = (100 - paddle_width / 2), (WIDTH - (100 - paddle_width / 2))
right_paddle_vel = left_paddle_vel = 0