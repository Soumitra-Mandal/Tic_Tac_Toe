# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:54:14 2021

@author: Soumitra
python - 3.8.8
pygame - 5.0.1

Tic-Tac-Toe Game
"""
# Initialising the pygame library
import pygame
pygame.init()

# Creating the display
screen = pygame.display.set_mode([480, 530])
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill((245,245,245))

# Coordinates to Draw the Xs and Os
position_coords = [(30,30),(190,30),(350,30),(30,190),(190,190),(350,190),(30,350),(190,350),(350,350)]
checked = [0 for i in range(9)] # Keeps check on which boxes are occupied
A = [0 for i in range(9)] # Keeps check which boxes Player A has occupied
B = [0 for i in range(9)] # Keeps check which boxes Player B has occupied


turn_list = ["Player B's TURN","Player A's TURN"] # Text to Generate for each turn
"""
Binary Logic is used to check winning conditions by using the decimal equivalent of A,B and checked.
"""
wins_list = [7,56,448,73,146,292,273,84,15,23,39,71,135,263,57,58,60,120,184,
             312,449,450,452,456,464,480,75,77,89,105,201,329,147,150,154,178,
             210,402,293,294,300,308,356,420,275,277,281,305,337,401,85,86,92,
             116,212,340,31,47,79,143,271,55,87,151,279,103,167,295,199,327,391,
             59,61,121,185,313,62,122,186,314,124,188,316,248,376,440,451,453,
             457,465,481,454,458,466,482,460,468,472,484,488,496,79,91,107,203,
             331,93,129,205,333,121,217,345,233,361,457,151,155,179,211,403,158,
             182,214,295,301,309,357,421,302,310,358,422,316,364,428,372,436,484,
             279,283,307,339,403,285,309,341,405,313,345,409,369,433,465,87,93,
             117,213,341,94,118,214,342,124,220,348,244,372,468]

# Array is sorted to reduce complexity
wins_list.sort()

# Custom Text Class
class Text:
    def __init__(self, fontName, fontSize, color):
        self.fontName = fontName
        self.fontSize = fontSize
        self.color = color
        
    def draw(self,screen,data,x,y):
        smallfont = pygame.font.SysFont(self.fontName,self.fontSize)
        text = smallfont.render(data , True , self.color)
        screen.blit(text,(x,y))

# Function to draw the grid layout
def drawGrid():
    pygame.draw.line(screen,"red",(160,0),(160,480),1)
    pygame.draw.line(screen,"red",(320,0),(320,480),1)
    pygame.draw.line(screen,"red",(0,160),(480,160),1)
    pygame.draw.line(screen,"red",(0,320),(480,320),1)
  
# Function to draw the Xs
def drawX(screen,pos):
    img = pygame.image.load("x.png")
    screen.blit(img,(pos[0],pos[1]))
    
# Function to draw the Os
def drawO(screen,pos):
    img = pygame.image.load('o.jpg')
    screen.blit(img,(pos[0],pos[1]))
drawer = [drawX,drawO]  

# Function to Convert mouse coords to Box number in which it was clicked 
def mouseToIndex(c):
    index = -1
    x = c[0]
    y = c[1]
    if(x<160 and y<160):
        index = 0
    elif(x<320 and y<160):
        index = 1
    elif(x<480 and y<160):
        index = 2
    elif(x<160 and y<320):
        index = 3
    elif(x<320 and y<320):
        index = 4
    elif(x<480 and y<320):
        index = 5
    elif(x<160 and y<480):
        index = 6
    elif(x<320 and y<480):
        index = 7
    elif(x<480 and y<480):
        index = 8
    return index

# Function to convert binary to decimal
def binaryToDecimal(l):
    num = 0
    for i in range(0,len(l)):
        num = num + (2**i)*(l[len(l)-i-1])
    return num

# Function called to show a tie/draw
def stalemate():
    stale_text = Text("Arial",20,(0,0,255))
    stale_text.draw(screen,"It is a tie", 405, 500)
    stale_text.draw(screen,"Space -> Reset", 220,500)

# Function to check for winner
def winner(W):
    win_text = Text("Arial",20,(245,0,0))
    win_text.draw(screen, W+' wins', 415,500)
    win_text.draw(screen,"Space -> Reset", 220,500)


turnText = Text("Arial",20,(0,0,0)) # Text used to print turns
turn = 0 # 0 for A's turn and 1 for B's turn
win = 0 # 1 if player A wins, 2 if player B wins

# Reset the game at any point of time
def reset():
    screen.fill((245,245,245))
    drawGrid()
    global checked
    global A
    global B
    global turn
    global win
    checked = [0 for i in range(9)]
    A = [0 for i in range(9)]
    B = [0 for i in range(9)]
    turn  = 0
    win = 0
running = True            
while running:
    drawGrid()
    # Break loop if user closed window
    for event in pygame.event.get():
        # Check if all boxes are filled and no one won
        if(binaryToDecimal(checked)==511 and win==0):
            stalemate()
        if event.type == pygame.QUIT:
            running = False     
        # Check for mouse Click
        if event.type == pygame.MOUSEBUTTONUP:
            c = mouseToIndex(pygame.mouse.get_pos())
            if(c>-1 and checked[c]==0):
                screen.fill((245,245,245), (40, 490, 125, 510))
                turnText.draw(screen,turn_list[turn],40,500)
                drawer[turn](screen,position_coords[c])
                checked[c] = 1
                if(turn==0):
                    A[c] = 1
                else:
                    B[c] = 1
                if(binaryToDecimal(A) in wins_list):
                    winner("A")
                    checked = [1 for x in checked]
                    win = 1
                elif(binaryToDecimal(B) in wins_list):
                    winner("B")
                    checked = [1 for x in checked]
                    win = 2
                turn = (turn+1)%2
        # Check if user clicked Space to Reset
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset()
            
                

    # Update the Screen
    pygame.display.flip()

# Quit the program
pygame.quit()

