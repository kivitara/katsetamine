
import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Foor - Anders Kivitar")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.rect(screen, [130,130,130], [100,15,100,270], 2)
    pygame.draw.circle(screen, [255,0,0], [150,65], 40)
    pygame.draw.circle(screen, [255,255,0], [150,150], 40)
    pygame.draw.circle(screen, [0,255,0], [150,235], 40)
    
    pygame.display.flip()

pygame.quit()

