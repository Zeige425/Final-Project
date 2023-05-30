import pygame
import sys
import random


pygame.init()


width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Air Hockey")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


paddle_width = 15
paddle_height = 80
paddle_speed = 5
puck_radius = 10
puck_speed = 3
score_1 = 0
score_2 = 0


paddle_1 = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_2 = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)


puck = pygame.Rect(width // 2 - puck_radius // 2, height // 2 - puck_radius // 2, puck_radius, puck_radius)
puck_direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_1.y > 0:
        paddle_1.y -= paddle_speed
    if keys[pygame.K_s] and paddle_1.y < height - paddle_height:
        paddle_1.y += paddle_speed
    if keys[pygame.K_UP] and paddle_2.y > 0:
        paddle_2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_2.y < height - paddle_height:
        paddle_2.y += paddle_speed

    
    puck.x += puck_direction[0] * puck_speed
    puck.y += puck_direction[1] * puck_speed

    
    if puck.colliderect(paddle_1) or puck.colliderect(paddle_2):
        puck_direction = (-puck_direction[0], puck_direction[1])


    if puck.y <= 0 or puck.y >= height - puck_radius:
        puck_direction = (puck_direction[0], -puck_direction[1])

    
    if puck.x < 0:
        score_2 += 1
        puck.center = (width // 2, height // 2)
        puck_direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
    if puck.x > width:
        score_1 += 1
        puck.center = (width // 2, height // 2)
        puck_direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])

  
    screen.fill(WHITE)

  
    pygame.draw.rect(screen, RED, paddle_1)
    pygame.draw.rect(screen, BLUE, paddle_2
