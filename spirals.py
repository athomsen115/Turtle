import math, turtle, random

ts = turtle.Screen()
ts.bgcolor('black')

colors = ['white', 'yellow', 'blue', 'orange', 'pink', 'red']
turt1 = turtle.Turtle()
turt1.speed(0)
turt1.color(colors[0])

turt2 = turtle.Turtle()
turt2.speed(0)
turt2.color(colors[1])

turt3 = turtle.Turtle()
turt3.speed(0)
turt3.color(colors[2])

turt4 = turtle.Turtle()
turt4.speed(0)
turt4.color(colors[3])

turt5 = turtle.Turtle()
turt5.speed(0)
turt5.color(colors[4])

turt6 = turtle.Turtle()
turt6.speed(0)
turt6.color(colors[5])

#rand = random.randint(0, 50)
run = True

while run:
    def drawCircles(turtle, size):
        for _ in range(10):
            turtle.circle(size)
            #size = size - rand + 62
            size = size - 10

    def drawSpecial(turtle, size, repeat):
        for _ in range(repeat):
            drawCircles(turtle, size)
            turtle.right(360/repeat)
    drawSpecial(turt1, 100, 10)
    
    def drawCircles(turtle, size):
        for _ in range(4):
            turtle.circle(size)
            #size = size - rand - 3
            size = size - 20

    def drawSpecial(turtle, size, repeat):
        for _ in range(repeat):
            drawCircles(turtle, size)
            turtle.right(360/repeat)
    drawSpecial(turt2, 100, 10)
    
    def drawCircles(turtle, size):
        for _ in range(4):
            turtle.circle(size)
            #size = size - rand
            size = size - 30

    def drawSpecial(turtle, size, repeat):
        for _ in range(repeat):
            drawCircles(turtle, size)
            turtle.right(360/repeat)
    drawSpecial(turt3, 100, 10)
    
    def drawCircles(turtle, size):
        for _ in range(4):
            turtle.circle(size)
            #size = size - rand + 2
            size = size - 40

    def drawSpecial(turtle, size, repeat):
        for _ in range(repeat):
            drawCircles(turtle, size)
            turtle.right(360/repeat)
    drawSpecial(turt4, 100, 10)
    
    def drawCircles(turtle, size):
        for _ in range(4):
            turtle.circle(size)
            #size = size - rand * 3
            size = size - 50

    def drawSpecial(turtle, size, repeat):
        for _ in range(repeat):
            drawCircles(turtle, size)
            turtle.right(360/repeat)
    drawSpecial(turt5, 100, 10)
    
    def drawCircles(turtle, size):
        for _ in range(4):
            turtle.circle(size)
            #size = size - rand - 45
            size = size - 60

    def drawSpecial(turtle, size, repeat):
        for _ in range(repeat):
            drawCircles(turtle, size)
            turtle.right(360/repeat)
    drawSpecial(turt6, 100, 10)
    
    run = False

    