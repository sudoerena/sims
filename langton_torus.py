# Langton's Ant on a torus plane

import pygame, sys, math
from pygame.locals import *

# colours
ANT=(255,0,0)       # "head"
LINE=(220,220,100)  # line
ON=(230,230,100)    # filled cell
OFF=(255,255,255)   # empty (unvisited) cell
MET=(255,255,200)   # empty (visited) cell
colour=OFF

# grid:
#   - a*a cells, including line pixel
#   - b*b raw cells
#   - n rows
#   - m columns
a=10
b=a-1
n=100
m=100

# (x,y): ant's current coordinates
#   - start at mid
x=math.floor(n/2)
y=math.floor(m/2)

#     0
#   3   1
#     2
# z: ant "facing" direction as above
z=0

# record value of each cell
val=[[False]*m for i in range(n)]

# initialize pygame; set display size and fill with empty
pygame.init()
DISPLAY=pygame.display.set_mode((a*n,a*m))
DISPLAY.fill(OFF)

# update:
#   - val   -- recolour
#   - z     -- turn
#   - x,y   -- move
def move():
    global x
    global y
    global z

    # recolour and turn
    if (val[x][y]):
        val[x][y]=False
        pygame.draw.rect(DISPLAY,MET,(a*x+1,a*y+1,b,b))
        z-=1
    else:
        val[x][y]=True
        pygame.draw.rect(DISPLAY,ON,(a*x+1,a*y+1,b,b))
        z+=1

    # move forward
    if (z%4==0):
        y+=1
    elif (z%4==1):
        x+=1
    elif (z%4==2):
        y-=1
    elif (z%4==3):
        x-=1
    else:
        print("ERROR\n")

    # loop back in bounds
    x=x%n
    y=y%m

    # draw ant head
    pygame.draw.rect(DISPLAY,ANT,(a*x+1,a*y+1,b,b))

    # redraw lines
    #pygame.draw.line(DISPLAY,ON,(a*i,0),(a*i,a*n),1)
    #pygame.draw.line(DISPLAY,ON,(0,a*j),(a*m,a*j),1)

# draw gridlines
def lines():
    global DISPLAY
    for i in range(n+1):
        for j in range(m+1):
            pygame.draw.line(DISPLAY,LINE,(a*i,0),(a*i,a*m),1)
            pygame.draw.line(DISPLAY,LINE,(0,a*j),(a*n,a*j),1)

def main():
    global colour
    global DISPLAY

    # initialize starting spot, gridlines
    val[x][y]=True
    pygame.draw.rect(DISPLAY,ANT,(a*x+1,a*y+1,b,b))
    lines()

    # infinite sim loop
    while True:
        move()

        # check quit
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# run main
main()
