from turtle import *

ts = Turtle()
ts.color('blue')
ts.speed('fastest')

def guideTurtle(radius, color, startpos=0):
    turt = Turtle()
    turt.speed('fastest')
    turt.color(color)
    turt.penup()
    turt.setposition(radius, startpos)
    turt.left(90)
    turt.pendown()
    return turt

def epitrochoid(rad1, rad2, num1, num2=1):
    turt1 = guideTurtle(rad1, 'blue')
    turt2 = guideTurtle(rad2, 'red', 30)
    
    def midpoint():
        return (0.5*(turt1.position() + turt2.position()))
    
    ts.penup()
    ts.setposition(midpoint())
    ts.pendown()
    
    N = 500
    steps = 360/N
    for _ in range(N):
        turt1.circle(rad1, num1*steps)
        turt2.circle(rad2, num2*steps)
        ts.setposition(midpoint())
        
def flowers():
    L = 6
    a, x = 50, 80
    ts.color('green')
    epitrochoid(a, L*a, L)
    ts.color('goldenrod')
    epitrochoid(a, L*a+x, L)
    ts.color('sienna')
    epitrochoid(a, L*a-x, L)
    
#epitrochoid(230, 300, 13, 8)
flowers()