import pygame
windowSize=(900,500)
win=pygame.display.set_mode(windowSize)

pygame.display.set_caption("Basket Ball Game") 

#images
pondf=pygame.image.load('pondf.png')

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)


def draw_window(ballInfo):
    blueBackground=(0, 255, 0) #rgb tuple
    win.fill(blueBackground)

    #blit puts one image on another
    win.blit(pondf, (700, 300))
    win.blit(bbball, (ballInfo.x, ballInfo.y))
    if ballInfo.x > 700 and ball.y >300:
        #print('You Win')
        msg= myfont.render('You Win', False, (0,0,0))
        
    else:
        msg= myfont.render('Move the ball to the pond(w,a,s,d)', False, (0,0,0))
    win.blit(msg, (200,50))
    pygame.display.update() #update the display


def main():
    ballInfo = pygame.Rect(0,0, 50, 50)  #x,y,width,height

    run= True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('User ended game')
                run=False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: 
            ballInfo.x -= 1
        elif keys_pressed[pygame.K_d]: 
            ballInfo.x += 1
        elif keys_pressed[pygame.K_w]: 
            ballInfo.y -= 1
        elif keys_pressed[pygame.K_s]: 
            ballInfo.y += 1
                
        draw_window(ballInfo)        
                
    pygame.quit()

main()
