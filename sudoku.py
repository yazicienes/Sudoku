import pygame

#constants
WIDTH = 550
BCKGRND_CLR = (251,250,250)
BLACK = (0,0,0)

def main():
    pygame.init()
    win = pygame.display.set_mode( (WIDTH, WIDTH) )
    pygame.display.set_caption( "Sudoku" )

    win.fill(BCKGRND_CLR)

    #draw grid
    for i in range(0,10):
        #                               x   ,   y
        pygame.draw.line(win, BLACK, (50 + 50*i, 50) , ( 50+50*i, 500) ,2 )#10 vertical lines
        pygame.draw.line(win, BLACK, (50, 50+50*i), (500, 50+50*i) )#horizontal lines
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()