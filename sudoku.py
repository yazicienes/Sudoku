import pygame
import requests #for get request to sudoku api

#constants
WIDTH = 550
BCKGRND_CLR = (251,250,250)
BLACK = (0,0,0)
BLUE = (128, 128, 128)

def main():

    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    grid = response.json()['board']
    grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid)) ]

    pygame.init()
    win = pygame.display.set_mode( (WIDTH, WIDTH) )
    pygame.display.set_caption( "Sudoku" )

    win.fill(BCKGRND_CLR)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    #draw grid
    for i in range(0,10):
        if (i%3==0):#every third line
            pygame.draw.line(win, BLACK, (50 + 50*i, 50) , ( 50+50*i, 500) , 4 )#vertical thick lines
            pygame.draw.line(win, BLACK, (50, 50+50*i), (500, 50+50*i) , 4 )#horizontal thick lines
        #                               x   ,   y
        pygame.draw.line(win, BLACK, (50 + 50*i, 50) , ( 50+50*i, 500) , 2 )#10 vertical lines
        pygame.draw.line(win, BLACK, (50, 50+50*i), (500, 50+50*i), 2 )#horizontal lines
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0<grid[i][j] <10):
                value = myfont.render(str(grid[i][j]), True, BLUE)
                win.blit(value, (j+1)*50+15, (i+1)*50+15)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()