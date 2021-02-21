import pygame
import requests #for get request to sudoku api, first need python -m pip install requests

#constants
WIDTH = 550
BCKGRND_CLR = (251,250,250)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] ==0:
                return (i,j) #row , col
    return None

def is_valid_num(grid, num, pos):
    #check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(pos)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #loop through that box
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if grid[i][j] == num and (i,j) != pos:
                return False
    return True

def solve_combination():
    pass

def solve_backtrack(win, grid):
    """
    Recursive function
    """
    print(grid)
    find = find_empty(grid)
    if not find:
        return True
    else:
        row,col = find
    
    for i in range(1,10):
        draw_sol(win, grid, i, (row,col))
        if is_valid_num(grid, i, (row,col)):
            grid[row][col] = i
            if solve_backtrack(win, grid):
                return True
            grid[row][col] = 0
    return False
    
def draw_sol(win, grid, num, pos):
    pygame.draw.rect(win, BCKGRND_CLR, ((pos[1]+1)*50+5, (pos[0]+1)*50+5, 50-10, 50-10))
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    value = myfont.render(str(num), True, BLACK)#mapping ascii to numeric values
    win.blit(value, ((pos[1]+1)*50+15, (pos[0]+1)*50))
    pygame.display.update()

def clear_sol(win, grid, num, pos):
    pygame.draw.rect(win, BCKGRND_CLR, (pos[0]*50+ 5, pos[1]*50+5, 50-10, 50-10))
    pygame.display.update()

def insert(win, position, grid_original):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type ==  pygame.KEYDOWN:
                #check if clicking the filled blocks
                if (grid_original[i-1][j-1] != 0):
                    return
                if ( 1<= event.key -48 < 10):#checking for valid input
                    pygame.draw.rect(win, BCKGRND_CLR, (position[0]*50+ 5, position[1]*50+5, 50-10, 50-10))
                    value = myfont.render(str(event.key-48), True, BLACK)#mapping ascii to numeric values
                    win.blit(value, (position[0]*50+15, position[1]*50))
                    pygame.display.update()
                    return
                return

def main():

    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    grid = response.json()['board'] #matrix of all the numbers - 9x9 matrix
    print (grid)
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

    #draw the numbers-skeleton
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0<grid[i][j] <10):
                value = myfont.render(str(grid[i][j]), True, BLUE)
                win.blit(value, ((j+1)*50+15, (i+1)*50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button ==1:
                pos = pygame.mouse.get_pos()
                insert(win, ((pos[0]//50), (pos[1]//50)), grid_original)#clicking anywhere in the block
            if event.type == pygame.QUIT:
                solve_backtrack(win, grid)
                pygame.quit()
                return


main()