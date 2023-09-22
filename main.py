from lib.utils.initials import *
from lib.classes.Ball import Ball

# skills
left_skill = right_skill = 0
left_skill_remaining = right_skill_remaining = 3
ball = Ball(WIDTH / 2 - radius, HEIGHT / 2 - radius, radius)
# MAIN LOOP
while run:
    wn.fill(BLACK)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.3
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.3
            if i.key == pygame.K_LEFT and right_skill_remaining > 0:
                right_skill = 1
            if i.key == pygame.K_RIGHT and right_skill_remaining > 0:
                right_skill = 2
            if i.key == pygame.K_w:
                left_paddle_vel = -0.3
            if i.key == pygame.K_s:
                left_paddle_vel = 0.3
            if i.key == pygame.K_d and left_skill_remaining > 0:
                left_skill = 1
            if i.key == pygame.K_a and left_skill_remaining > 0:
                left_skill = 2
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # BALL'S MOVEMENT CONTROLS old
    """if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        player1_score += 1
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.35, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.25, 0.35
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.35, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.25, 0.35

    if ball_x <= 0 + radius:
        player2_score += 1
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        ball_vel_x, ball_vel_y = 0.2, 0.2
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.35, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.25, 0.35
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.35, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.25, 0.35"""

    # PADDLE's MOVEMENT CONTROL
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # PADDLE COLLISIONS
    # left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    # right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    # skill execution
    if left_skill == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -2.5
                left_skill = 0
                left_skill_remaining -= 1
    elif left_skill == 2:
        left_paddle_y = ball_y
        left_skill = 0
        left_skill_remaining -= 1

    if right_skill == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_vel_x *= -2.5
                right_skill = 0
                right_skill_remaining -= 1
    elif right_skill == 2:
        right_paddle_y = ball_y
        right_skill = 0
        right_skill_remaining -= 1

    # movement
    ball.move()
    ball.check_collisions(left_paddle_x, left_paddle_y, right_paddle_x, right_paddle_y, paddle_width, paddle_height)
    ball.reset()
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

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

    # objects
    pygame.draw.circle(wn, BLUE, (ball.x, ball.y), ball.radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    if left_skill == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_skill == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

    # Endscreen
    winning_font = pygame.font.SysFont('callibri', 80)
    if player1_score >=5:
        wn.fill(BLACK)
        endscreen = winning_font.render("Player 1 WON !!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
    if player2_score >=5:
        wn.fill(BLACK)
        endscreen = winning_font.render("Player 2 WON !!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
    

    pygame.display.update()
