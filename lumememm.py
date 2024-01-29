
import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
            
    #screen.fill([204, 255, 255])
    pygame.draw.rect(screen, [130,130,130], [100,15,100,270], 2)
    pygame.draw.circle(screen, [255,0,0], [150,65], 40)
    pygame.draw.circle(screen, [255,255,0], [150,150], 40)
    pygame.draw.circle(screen, [0,255,0], [150,235], 40)
    
    #pygame.draw.circle(screen, [0,0,0], [140,75], 5)
    #pygame.draw.circle(screen, [0,0,0], [160,75], 5)
    
    #pygame.draw.polygon(screen, [255,0,0], [[145,85], [150,100], [155,85]])
    
    pygame.display.flip()

pygame.quit()

