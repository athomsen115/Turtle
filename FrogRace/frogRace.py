import turtle, random, sys

WIDTH = 600
HEIGHT = 600
frogs = 8

screen = turtle.Screen()
screen.screensize(WIDTH, HEIGHT)
screen.title("Frog Race")
frog1 = 'frog1.gif'
frog2 = 'frog2.gif'
frog3 = 'frog3.gif'
frog4 = 'frog4.gif'
frog5 = 'frog5.gif'
frog6 = 'frog6.gif'
frog7 = 'frog7.gif'
frog8 = 'frog8.gif'


screen.register_shape(frog1)
screen.register_shape(frog2)
screen.register_shape(frog3)
screen.register_shape(frog4)
screen.register_shape(frog5)
screen.register_shape(frog6)
screen.register_shape(frog7)
screen.register_shape(frog8)


class Racer(object):
    def __init__(self, color, pos, shape):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape(shape)
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        #self.turt.setheading(0)
        
    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0] + r, self.pos[1])
        self.turt.pendown()
        self.turt.forward(r)
    
    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)
    
def setupFile(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()
    
def startGame():
    frogList = []
    screen.clearscreen()
    colors = ["cyan", "gold", "magenta", "turquoise", "black", "blue", "red", "yellow"]
    shapes = [frog1, frog2, frog3, frog4, frog5, frog6, frog7, frog8]
    start = -(HEIGHT/2) + 30
    for t in range(frogs):
        posY = start + t*(HEIGHT)//frogs
        frogList.append(Racer(colors[t], (-280, posY), shapes[t]))
        frogList[t].turt.showturtle()
        
    run = True
    while run:
        for t in frogList:
            t.move()
        
        maxColor = []
        maxDis = 0
        for t in frogList:
            if t.pos[0] > 230 and t.pos[0] > maxDis:
                maxDis = t.pos[0]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[0] > 230 and t.pos[0] == maxDis:
                maxDis = t.pos[0]
                maxColor.append(t.color)
        
        if len(maxColor) > 0:
            run = False
            print("The winner is: ")
            for win in maxColor:
                print(win)
                
    oldScore = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldScore.append([color, score])
    file.close()
    
    file = open('scores.txt', 'w')
    for entry in oldScore:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1
        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')    
    file.close()
    
start = input('Would you like to play a game? ')
if start.lower().startswith('y'):
    startGame()
else:
    sys.exit()


while True:
    print('----------------------------------')
    start = input("Would you like to play again?")
    if start.lower().startswith('y'):
        startGame()
    else: 
        break