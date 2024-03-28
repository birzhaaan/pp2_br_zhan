'''import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen, (0, 128, 255),(100,100),100)
    pygame.display.flip()
import pygame
pygame.init()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode((800,600))
done = False
is_red = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_red = not is_red
        if is_red:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(30,30,100,60))
        else:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 30, 100, 60))
        pygame.display.flip()'''







import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
finished = False
background = pygame.image.load('C:/Users/user/Desktop/pp2/LAB7/Images/clock.png')
second_hand = pygame.image.load('C:/Users/user/Desktop/pp2/LAB7/Images/lhand.png')
minute_hand = pygame.image.load('C:/Users/user/Desktop/pp2/LAB7/Images/rhand.png')
clock_center = (415, 418)

while not finished:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    current_time = datetime.now().time()

    second_angle = -(current_time.second * 6)
    minute_angle = -(current_time.minute * 6) - (current_time.second / 10)
    hour_angle = -(current_time.hour * 30) - (current_time.minute / 2)

    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)
    sec_rect = rotated_second_hand.get_rect()
    sec_rect.center = clock_center
    screen.blit(rotated_second_hand, sec_rect.topleft)

    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    min_rect = rotated_minute_hand.get_rect()
    min_rect.center = clock_center
    screen.blit(rotated_minute_hand, min_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
