import turtle

'initializes turtle and screen'
def initialize_turtle():
    s = turtle.getscreen()
    t = turtle.Turtle()
    return t

'draws square of length 80 from x, y co ordinate'
'x and y are float variables and t is the turtle'
def draw_square(t: turtle, x, y) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("green")
    t.goto(x + 80, y)
    t.goto(x + 80, y - 80)
    t.goto(x, y - 80)
    t.goto(x, y)

'Draws a circle starting from the center of the bottom edge of the square'
def draw_circle(t: turtle, x, y) -> None:
    t.penup()
    t.goto(x + 40, y - 80)
    t.pendown()
    t.pencolor("red")
    t.circle(40)

'Take new x and y co-ordinates from the user for square and circle'

def input_to_user(t):
    x_sq = float(input("What x co-od do you want to move square to? "))
    y_sq = float(input("What y co-od do you want to move square to? "))
    x_circ = float(input("What x co-od do you want to move circle to? "))
    y_circ = float(input("What y co-od do you want to move circle to? "))
    t.clear()
    draw_square(t, x_sq, y_sq)
    draw_circle(t, x_circ, y_circ) 


    
    
    


    
    
    
    
