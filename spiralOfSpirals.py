import turtle

turt = turtle.Turtle()
turt.speed(10)
turt.shape('turtle')
turt.penup()
ts = turtle.Screen()
ts.bgcolor('black')

sides = int(input("How many side do you want in your spiral? (2-6)"))
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

for i in range(50):
    turt.forward(i*4)
    pos = turt.position()
    heading = turt.heading()
    #print(pos, heading)
    for j in range(int(i/2)):
        turt.pendown()
        turt.color(colors[j%sides])
        turt.forward(2*j)
        turt.right(360/sides-2)
        turt.penup()
    turt.setx(pos[0])
    turt.sety(pos[1])
    turt.setheading(heading)
    turt.left(360/sides + 2)
    