import pygame as pg
import time
pg.init()

screen = pg.display.set_mode((300, 400))
pg.display.set_caption('Froags')
font = pg.font.Font(None, 32)

player_pos = pg.Vector2(150, 300)
score = 0

car_pos = pg.Vector2(150, 200)
car2_pos = pg.Vector2(150, 100)

train_pos = pg.Vector2(150, 35)

run = True
while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
			
	if car_pos.x >= 300:
		car_pos.x = 0
	if car2_pos.x <= 0:
		car2_pos.x = 300
		
	if train_pos.x >= 300:
		train_pos.x = 0
		
	car_pos.x += 0.1
	car2_pos.x -= 0.1
	
	train_pos.x += 0.5
	
	keys = pg.key.get_pressed()
	if keys[pg.K_w]:
		player_pos.y -= 0.1
	if keys[pg.K_a]:
		player_pos.x -= 0.1
	if keys[pg.K_d]:
		player_pos.x += 0.1
	if keys[pg.K_LCTRL]:
		player_pos.y -= 0.5
	
	if player_pos.y <= 0:
		player_pos.y = 400
		score += 1
	
	player_rect = pg.Rect(player_pos.x, player_pos.y, 30, 30)
	car_rect = pg.Rect(car_pos.x, car_pos.y, 75, 50)
	car2_rect = pg.Rect(car2_pos.x, car2_pos.y, 75, 50)
	train_rect = pg.Rect(train_pos.x, train_pos.y, 100, 50)
	
	if player_rect.colliderect(car_rect) or player_rect.colliderect(car2_rect):
		time.sleep(1)
		run = False
	
	if keys[pg.K_SPACE] and player_rect.colliderect(train_rect):
		player_pos.x = train_pos.x
	elif player_rect.colliderect(train_rect):
		time.sleep(1)
		run = False
	
	screen.fill((0, 0, 0))
	pg.draw.rect(screen, (255, 0, 255), train_rect)
	pg.draw.rect(screen, (0, 255, 0), player_rect)
	pg.draw.rect(screen, (255, 0, 0), car_rect)
	pg.draw.rect(screen, (0, 0, 255), car2_rect)
	screen.blit(font.render(f'Score: {score}', True, (255, 255, 255)), (20, 20))
	
	pg.display.flip()

pg.quit()

