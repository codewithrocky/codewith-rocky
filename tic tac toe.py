import pygame
import sys
import numpy as np

pygame.init()

width=700
height=700
BOARD_ROWS=3
BOARD_COLS=3
SQUARE_SIZE=width//BOARD_COLS
RED=(255,0,0)
LightBlue=(28,170,156)
LINECOLOR=(23,145,135)
LINEWIDTH=15
CIRCLE_RADIUS=SQUARE_SIZE//3
CIRCLE_WIDTH=15
WHITE=(255,255,255)
CROSS_WIDTH=25
SPACE=SQUARE_SIZE//4# SPACE OF CROSS'S LINES AND CORNERS




screen= pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic Tac Toe by Saanvi")
screen.fill(LightBlue)

#board
board=np.zeros((BOARD_ROWS,BOARD_COLS))#it will be the list of units of tic tac toe 
#print(board)


#pygame.draw.line(screen,RED,(10,10),(300,300),10)

def draw_lines():
    pygame.draw.line(screen, LINECOLOR,(0,SQUARE_SIZE),(width,SQUARE_SIZE),LINEWIDTH)#1st horizontal line
    pygame.draw.line(screen, LINECOLOR,(0,2*SQUARE_SIZE),(width,2*SQUARE_SIZE),LINEWIDTH)# 2nd horizontal line
    pygame.draw.line(screen, LINECOLOR,(SQUARE_SIZE,0),(SQUARE_SIZE,height),LINEWIDTH)#1st vertical line
    pygame.draw.line(screen, LINECOLOR,(2*SQUARE_SIZE,0),(2*SQUARE_SIZE,height),LINEWIDTH)# 2nd vertical line
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen,WHITE,(int(col*SQUARE_SIZE+SQUARE_SIZE/2),int(row*SQUARE_SIZE+SQUARE_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen,RED,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,RED,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),CROSS_WIDTH)

def mark_square(row,col,player):
    board[row][col]= player
def available_sqaure(row,col):
    if board[row][col]==0:
        return True
    else:
        return False
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==0:
                return False
    return True
def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_winning_line(col,player)
            return True
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True
    # ascending diagnol win check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagnol(player)
        return True
    #descending diagnol win check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagnol(player)
        return True

    return False
        

def draw_vertical_winning_line(col,player):
    posX=col*SQUARE_SIZE+SQUARE_SIZE//2
    if player==1:
        color=WHITE
    elif player==2:
        color=RED

    pygame.draw.line(screen,color,(posX,15),(posX,height-15),15)
        
def draw_horizontal_winning_line(row,player):
     posY=row*SQUARE_SIZE+SQUARE_SIZE//2
     if player==1:
         color=WHITE
     elif player==2:
         color=RED
     pygame.draw.line(screen,color,(15,posY),(width-15,posY),15)
    
def draw_asc_diagnol(player):
    if player==1:
        color=WHITE
    elif player==2:
        color=RED

    pygame.draw.line(screen,color,(15,height-15),(width-15,15),15)
def draw_desc_diagnol(player):
    if player==1:
        color=WHITE
    elif player==2:
        color=RED
    pygame.draw.line(screen,color,(15,15),(width-15,height-15),15)
def restart():
    screen.fill(LightBlue)
    draw_lines()
    player=1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0
            
    
    


draw_lines()

player=1
game_over=False
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX=event.pos[0]#x coordinate # event.pos gets the position of the cursor
            mouseY=event.pos[1]#y coordinate

            clicked_row=int(mouseY // SQUARE_SIZE)
            clicked_col=int(mouseX // SQUARE_SIZE)

            print(clicked_row)
            print(clicked_col)

            if available_sqaure(clicked_row,clicked_col):
                mark_square(clicked_row,clicked_col,player)
                if check_win(player):
                    game_over=True

                player=player%2+1


                draw_figures()
                
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                game_over=False
                restart()

    pygame.display.update()
