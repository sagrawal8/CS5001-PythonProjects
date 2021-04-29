'''
Name: Shashank Agrawal
Class: CS 5001
Program: shape_clicker
'''

from PositionService import *
import turtle

t = turtle.Turtle()  #global turtle 

	
'''
Function: drawCircle
Parameters: x - x co-ordinate
            y - y co-ordinate
Returns: None
Does: Draws a circle with x, y as center
'''
def drawCircle(x, y):
    t.penup()
    t.goto(x, y - 80)
    t.pendown()
    t.pencolor("green")
    t.circle(80)    

'''
Function: getClick
Parameters: x - x co-ordinate
            y - y co-ordinate
Returns: None
Does: Prints co-ordinate of mouse click
      If the co-ordinate lies outside circle, new cricle is drawn and prev one is erased
      and center of circle is updated to show center of new circle
      If the co-ordinate lies inside circle, prev circle is erased 
'''    
def getClick(x, y):
    print("Co-od clicked are", x, " &", y)
    if(x < (get_position_x() - 80) or x > (get_position_x() + 80)):  #check if x cordinate is outside range
        t.clear()
        drawCircle(x, y)
        set_position(x, y)
        
    elif(y < (get_position_y() - 80) or x > (get_position_y() + 80)):  #check if y co-od is outside range
        t.clear()   
        drawCircle(x, y)
        set_position(x, y)
    else:
        t.clear()        #if within range, clear circle


def main():
    global t
    screen = turtle.getscreen()
    drawCircle(0, 0)                 #draw circle at 0,0
    screen.onclick(getClick)    
    

main()
    


    
