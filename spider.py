import turtle, math

turt = turtle.Turtle()
turt.speed(0)
turt.color('blue')
size=200

turt.setheading(90)
for i in range(0, 6):
    turt.forward(size)
    turt.penup()
    turt.forward(-size)
    turt.left(60)
    turt.pendown()
    
turt.setheading(90)
turt.forward(size)
turt.setheading(215)
newSize = (size*(math.sqrt(3)/2)) / math.sin(math.radians(65))
for i in range(0, 30):
    turt.forward(newSize)
    turt.left(60)
    newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))
