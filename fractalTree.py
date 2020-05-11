import turtle, random

myTurtle = turtle.Turtle()
myTurtle.screen.bgcolor('red')
myTurtle.left(90)
myTurtle.speed(20)
myTurtle.color('green')
myTurtle.pensize(5)
myTurtle.screen.title("My Fractal Tree")

def drawFractal(distance):
    #option to make a multicolored tree if desired
    colors = ["green", "blue", "yellow", "pink", "orange", "purple", "white", "magenta"]
    myTurtle.color(random.choice(colors))
    
    if distance < 10:
        return
    else:
        myTurtle.forward(distance)
        myTurtle.left(30)
        drawFractal(3*distance/4)
        myTurtle.right(60)
        drawFractal(3*distance/4)
        myTurtle.left(30)
        myTurtle.backward(distance)
        

drawFractal(80)
myTurtle = turtle.done()