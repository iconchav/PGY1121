import sys, pygame

pygame.init()

size = width, height = 800,600
speed = [2, 2]
bg = [255, 255, 255]

screen = pygame.display.set_mode(size)
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT): sys.exit()
        if (event.type == pygame.KEYDOWN): 
            if(event.key == pygame.K_ESCAPE):
                sys.exit()
    ballrect = ballrect.move(speed)
    if(ballrect.left<0 or ballrect.right>width):
        speed[0] = -speed[0]
    if(ballrect.top<0 or ballrect.bottom>height):
        speed[1] = -speed[1]
    screen.fill(bg)
    screen.blit(ball,ballrect)
    pygame.display.flip()
