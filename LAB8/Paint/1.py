
import pygame 
pygame.init()


WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

COLOR = RED   


clock = pygame.time.Clock()
FPS = 30


prev, cur = None, None  
prev1, cur1 = None, None 


l, w = 1001, 601
screen = pygame.display.set_mode((l,w))
screen.fill(WHITE)
running = True


pen = None
last_event = None


while running:
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pen = "mouse"
			if event.key == pygame.K_w:
				pen = "rect"
			if event.key == pygame.K_e:
				pen = "circle"
			if event.key == pygame.K_r:
				pen = "eraser"
				
			
			if event.key == pygame.K_z:
				COLOR = RED
			if event.key == pygame.K_x:
				COLOR = GREEN
			if event.key == pygame.K_c:
				COLOR  = BLUE
			if event.key == pygame.K_v:
				COLOR = BLACK
				
		
		if pen == "mouse" :
			if event.type == pygame.MOUSEBUTTONDOWN:
				prev = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEMOTION:
				cur = pygame.mouse.get_pos()
			if prev:
				pygame.draw.line(screen, COLOR, prev, cur, 1)
				prev = cur
			if event.type == pygame.MOUSEBUTTONUP:
				prev = None
				
		
		if pen == "rect":
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y =pygame.mouse.get_pos()
				last_event = "DOWN"
			if event.type == pygame.MOUSEBUTTONUP:
				x1, y1 =pygame.mouse.get_pos()
				last_event = "UP"
			if last_event == "UP":
				pygame.draw.rect(screen, COLOR, (int(x), int(y), int(x1)-int(x), int(y1)-int(y) ))
				last_event = 'None'
				
		
		if pen == "circle" :
			if event.type == pygame.MOUSEBUTTONDOWN:
				x2, y2 =pygame.mouse.get_pos()
				last_event = "DOWN"
			if event.type == pygame.MOUSEBUTTONUP:
				x3, y3 =pygame.mouse.get_pos()
				last_event = "UP"
			if last_event == "UP":
				pygame.draw.circle(screen, COLOR, (x2+(x3-x2)/2, y2+(y3-y2)/2), (x3-x2)/2 )
				last_event = 'None'
				
		
		if pen == "eraser" :
			if event.type == pygame.MOUSEBUTTONDOWN:
				prev1 = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEMOTION:
				cur1 = pygame.mouse.get_pos()
			if prev1:
				pygame.draw.line(screen, WHITE, prev1, cur1, 10)
				prev1 = cur1
			if event.type == pygame.MOUSEBUTTONUP:
				prev1 = None
				
				
				
				
	pygame.display.flip()
	
	
	clock.tick(30)
	
	
pygame.quit()