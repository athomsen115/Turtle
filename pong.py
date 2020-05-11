#A simple graphical pong game

import turtle
#import os  ## For sound play on Linux
#import winsound  ## For sound play on Windows

screen = turtle.Screen()
screen.title("Bringing back the 70's: Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#Paddle A
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

#Paddle B
player2 = turtle.Turtle()
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# Scoring Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

#Score
scorePlayer1 = 0
scorePlayer2 = 0

# Moving Paddle A Functions
def player1Up():
    y = player1.ycor()
    y += 20
    player1.sety(y)
    
def player1Down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)


# Moving Paddle B Functions
def player2Up():
    y = player2.ycor()
    y += 20
    player2.sety(y)
    
def player2Down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

#Keyboard Binding
screen.listen()
screen.onkeypress(player1Up, "w")
screen.onkeypress(player1Down, "s")
screen.onkeypress(player2Up, "Up")
screen.onkeypress(player2Down, "Down")

#Game Loop
while True:
    screen.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx *= -1
        scorePlayer1 += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(scorePlayer1, scorePlayer2), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1 
        scorePlayer2 += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(scorePlayer1, scorePlayer2), align="center", font=("Courier", 24, "normal"))
    
    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 
        #os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)