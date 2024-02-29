import pygame

pygame.init()

w = 1000
h = 500

screen = pygame.display.set_mode((w, h))

rodando = True

while rodando:
    for event in pygame.event.get():
         if event == pygame.QUIT:
             rodando = False
    
   
   
    screen.fill("#ffffff")    
    pygame.display.flip()
pygame.quit()