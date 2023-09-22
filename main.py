from lib.utils.initials import *
from lib.classes.Ball import Ball
from lib.classes.Paddle import Paddle

ball = Ball(WIDTH / 2 - radius, HEIGHT / 2 - radius, radius)
left_paddle = Paddle(left_paddle_x, left_paddle_y)
right_paddle = Paddle(right_paddle_x, right_paddle_y)
# MAIN LOOP
while run:
    wn.fill(BLACK)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle.vel = -0.95
            if i.key == pygame.K_DOWN:
                right_paddle.vel = 0.95
            if i.key == pygame.K_LEFT and right_skill_remaining > 0:
                right_skill = 1
            if i.key == pygame.K_RIGHT and right_skill_remaining > 0:
                right_skill = 2
            if i.key == pygame.K_w:
                left_paddle.vel = -0.95
            if i.key == pygame.K_s:
                left_paddle.vel = 0.95
            if i.key == pygame.K_d and left_skill_remaining > 0:
                left_skill = 1
            if i.key == pygame.K_a and left_skill_remaining > 0:
                left_skill = 2
        if i.type == pygame.KEYUP:
            right_paddle.vel = 0
            left_paddle.vel = 0

    # PADDLE's MOVEMENT CONTROL
    left_paddle.collisions()
    right_paddle.collisions()

    # skill execution
    if left_skill == 1:
        if left_paddle.x_pos <= ball.x <= left_paddle.x_pos + paddle_width:
            if left_paddle.y_pos <= ball.y <= left_paddle.y_pos + paddle_height:
                ball.x = left_paddle.x_pos + paddle_width
                ball.velocity_x *= 3.5
                left_skill = 0
                left_skill_remaining -= 1
    elif left_skill == 2:
        left_paddle.y_pos = ball.y
        left_skill = 0
        left_skill_remaining -= 1

    if right_skill == 1:
        if right_paddle.x_pos <= ball.x <= right_paddle.x_pos + paddle_width:
            if right_paddle.y_pos <= ball.y <= right_paddle.y_pos + paddle_height:
                ball.x = right_paddle.x_pos
                ball.velocity_x *= 3.5
                right_skill = 0
                right_skill_remaining -= 1
    elif right_skill == 2:
        right_paddle.y_pos = ball.y
        right_skill = 0
        right_skill_remaining -= 1

    # movement
    ball.move()
    ball.check_collisions(left_paddle, right_paddle)
    ball.reset()
    left_paddle.y_pos += left_paddle.vel
    right_paddle.y_pos += right_paddle.vel

    # objects
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()

    # scoreboard
    font = pygame.font.SysFont('callibri', 32)
    score_1 = font.render(f"Player 1: {str(player1_score)}", True, WHITE)
    wn.blit(score_1, (25, 25))
    score_2 = font.render(f"Player 2: {str(player2_score)}", True, WHITE)
    wn.blit(score_2, (855, 25))
    skill_left_1 = font.render(f"Skill uses remaining: {str(left_skill_remaining)}", True, WHITE)
    wn.blit(skill_left_1, (25, 65))
    skill_left_2 = font.render(f"Skill uses remaining: {str(right_skill_remaining)}", True, WHITE)
    wn.blit(skill_left_2, (730, 65))

    if left_skill == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle.x_pos + 10, left_paddle.y_pos + 10), 4)
    if right_skill == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle.x_pos + 10, right_paddle.y_pos + 10), 4)

    # Endscreen
    winning_font = pygame.font.SysFont('callibri', 80)
    if player1_score >= 5:
        wn.fill(BLACK)
        endscreen = winning_font.render("Player 1 WON !!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
    if player2_score >= 5:
        wn.fill(BLACK)
        endscreen = winning_font.render("Player 2 WON !!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))

    pygame.display.update()
