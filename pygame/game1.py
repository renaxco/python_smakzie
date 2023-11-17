import pygame

pygame.init()
win = pygame.display.set_mode((700,700))

pygame.display.set_caption('Game Saya 1')

x = 330
y = 320
width = 40 
height = 60
vel = 10

run = True
while run:
  pygame.time.delay(100)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    x -= vel
  if keys[pygame.K_a]:
    x += vel
  if keys[pygame.K_UP]:
    y -= vel
  if keys[pygame.K_DOWN]:
    y += vel

  win.fill((255,255,255))
  pygame.draw.rect(win, (125,30,255), (x, y, width, height) )
  pygame.display.update()