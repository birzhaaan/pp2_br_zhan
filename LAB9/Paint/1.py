import pygame

pygame.init()

paintings = []

timer = pygame.time.Clock()
fps = 60

active_color = (0, 0, 0)
active_shape = 0

window_width = 800
window_height = 600

screen = pygame.display.set_mode([window_width, window_height])

pygame.display.set_caption("Drawing App")

def draw_display():
    pygame.draw.rect(screen, 'gray', [0, 0, window_width, 100])
    pygame.draw.line(screen, 'black', [0, 100], [window_width, 100])
    rect_button = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])
    circle_button = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    pygame.draw.circle(screen, 'white', [140, 50], 30)
    triangle_button = [pygame.draw.rect(screen, 'black', [200, 10, 80, 80]), 2]
    pygame.draw.polygon(screen, 'white', ((240, 90), (200, 50), (280, 50)))
    rhombus_button = [pygame.draw.rect(screen, 'black', [300, 10, 80, 80]), 3]
    pygame.draw.polygon(screen, 'white', ((320, 50), (360, 90), (400, 50), (360, 10)))
    blue_button = [pygame.draw.rect(screen, (0, 0, 255), [window_width - 35, 10, 25, 25]), (0, 0, 255)]
    red_button = [pygame.draw.rect(screen, (255, 0, 0), [window_width - 35, 35, 25, 25]), (255, 0, 0)]
    green_button = [pygame.draw.rect(screen, (0, 255, 0), [window_width - 60, 10, 25, 25]), (0, 255, 0)]
    yellow_button = [pygame.draw.rect(screen, (255, 255, 0), [window_width - 60, 35, 25, 25]), (255, 255, 0)]
    black_button = [pygame.draw.rect(screen, (0, 0, 0), [window_width - 85, 10, 25, 25]), (0, 0, 0)]
    purple_button = [pygame.draw.rect(screen, (255, 0, 255), [window_width - 85, 35, 25, 25]), (255, 0, 255)]
    eraser_button = [pygame.draw.rect(screen, (255, 255, 255), [window_width - 150, 20, 25, 25]), (255, 255, 255)]
    return [blue_button, red_button, green_button, yellow_button, black_button, purple_button, eraser_button], [rect_button, circle_button, triangle_button, rhombus_button]

def draw_paintings(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15)
        if paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30])
        if paint[2] == 2:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-10, paint[1][1]+10), (paint[1][0], paint[1][1]-10), (paint[1][0]+10, paint[1][1]+10)))
        if paint[2] == 3:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-20, paint[1][1]), (paint[1][0], paint[1][1]-20), (paint[1][0]+20, paint[1][1]), (paint[1][0], paint[1][1]+20)))

def draw():
    global active_color, active_shape, mouse_pos
    if mouse_pos[1] > 100:
        if active_shape == 0:
            pygame.draw.rect(screen, active_color, [mouse_pos[0]-15, mouse_pos[1]-15, 30, 30])
        if active_shape == 1:
            pygame.draw.circle(screen, active_color, mouse_pos, 15)
        if active_shape == 2:
            pygame.draw.polygon(screen, active_color, ((mouse_pos[0]-10, mouse_pos[1]+10), (mouse_pos[0], mouse_pos[1]-10), (mouse_pos[0]+10, mouse_pos[1]+10)))
        if active_shape == 3:
            pygame.draw.polygon(screen, active_color, ((mouse_pos[0]-20, mouse_pos[1]), (mouse_pos[0], mouse_pos[1]-20), (mouse_pos[0]+20, mouse_pos[1]), (mouse_pos[0], mouse_pos[1]+20)))

run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    colors, shapes = draw_display()

    mouse_pos = pygame.mouse.get_pos()
    draw()
    
    click = pygame.mouse.get_pressed()[0]
    if click and mouse_pos[1] > 100:
        paintings.append((active_color, mouse_pos, active_shape))
    draw_paintings(paintings)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paintings = []

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    active_color = i[1]
            for i in shapes:
                if i[0].collidepoint(event.pos):
                    active_shape = i[1]
    
    pygame.display.flip()
