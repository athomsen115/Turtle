import math, turtle, random, argparse
from datetime import datetime
from fractions import gcd
from PIL import Image

ts = turtle.Screen()
myturtle = turtle.Turtle()

class Spiro():
    def __init__(self, xc, yc, col, Radii, radii, l):
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.step = 5
        self.drawingComplete = False
        self.setParams(xc, yc, col, Radii, radii, l)
        self.restart()
        
    def setParams(self, xcurve, ycurve, color, Radii, radii, l):
        self.xcurve = xcurve
        self.ycurve = ycurve
        self.color = color
        self.Radii = int(Radii)
        self.radii = int(radii)
        self.l = l 
        
        gcdValue = gcd(self.radii, self.Radii)
        self.nRotation = self.radii // gcdValue
        self.k = radii/float(Radii)
        self.turt.color(*color)
        self.angle = 0
    
    def restart(self):
        self.drawingComplete = False
        self.turt.showturtle()
        self.turt.up()
        Radii, k, l = self.Radii, self.k, self.l
        angle = 0.0
        x = Radii*((1-k)*math.cos(angle) + l*k*math.cos((1-k)*angle/k))
        y = Radii*((1-k)*math.sin(angle) + 1*k*math.sin((1-k)*angle/k))
        self.turt.setpos(self.xcurve + x, self.ycurve + y)
        self.turt.down()
    
    def draw(self):
        Radii, k, l = self.Radii, self.k, self.l
        for i in range(0, 360*self.nRotation + 1, self.step):
            angle = math.radians(i)
            x = Radii*((1-k)*math.cos(angle) + l*k*math.cos((1-k)*angle/k))
            y = Radii*((1-k)*math.sin(angle) + 1*k*math.sin((1-k)*angle/k))
            self.turt.setpos(self.xcurve + x, self.ycurve + y)
            # add direction vector calculation and reorient the turle
        self.turt.hideturtle()
        
    def update(self):
        if self.drawingComplete:
            return 
        
        self.angle += self.step
        Radii, k, l = self.Radii, self.k, self.l
        angle = math.radians(self.angle)
        x = Radii*((1-k)*math.cos(angle) + l*k*math.cos((1-k)*angle/k))
        y = Radii*((1-k)*math.sin(angle) + 1*k*math.sin((1-k)*angle/k))
        self.turt.setpos(self.xcurve + x, self.ycurve + y)
        
        if self.angle > 360*self.nRotation:
            self.drawingComplete = True
            self.turt.hideturtle()
            
    def clear(self):
        self.turt.clear()

class SpiroAnimator():
    def __init__(self, num):
        self.deltaTime = 10
        self.width = ts.window_width()
        self.height = ts.window_height()
        self.spiros = []
        for _ in range(num):
            rparams = self.genRandomParams()
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            
        ts.ontimer(self.update, self.deltaTime)
    
    def genRandomParams(self):    
        width, height = self.width, self.height
        Radii = random.randint(50, min(width, height)//2)
        radii = random.randint(10, 9*Radii//10)
        l = random.uniform(0.1, 0.9)
        xcurve = random.randint(-width//2, width//2)
        ycurve = random.randint(-height//2, height//2)
        color = (random.random(), random.random(), random.random())
        
        return (xcurve, ycurve, color, Radii, radii, l)
    
    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
            rparams = self.genRandomParams()
            spiro.setparams(*rparams)
            spiro.restart()
    
    def update(self):
        numComplete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawingComplete:
                numComplete += 1
        if numComplete == len(self.spiros):
            self.restart()
        ts.ontimer(self.update(), self.deltaTime)
    
    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.turt.isvisible():
                spiro.turt.hideturtle()
            else:
                spiro.turt.showturtle()
    
def saveDrawing():
    myturtle.hideturtle()
    dateString = (datetime.now()).strftime("%d%b%Y - %H%M%S")
    fileName = 'spiro-' + dateString
    print("Saving drawing to %s.eps/png" % fileName)
    canvas = ts.getcanvas()
    canvas.postscript(file = fileName + '.eps')
    image = Image.open(fileName + '.eps')
    image.save(fileName + 'png', 'png')
    myturtle.showturtle()
    
def getPlayerInput():
    while True:
        var = input("Please enter R (ex. 300), r (ex. 100), and l (ex. 0.9), (or nothing for random output): ")
        var = var.split()
        if len(var) == 3 and var[0].isdigit() and var[1].isdigit():
            return float(var[0]), float(var[1]), float(var[2])
        else:
            return None, None, None

def main():
    descStr = """This program draws spirographs using the turtle module. 
    When run with no arguments, this program draws random spirographs. 
    
    Terminology:
    R = radius of outer circle
    r = radius of inner circle
    l = ratio of hole distance to r
    """
    """
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False, help="The three arguments in sparams: R, r, l")
    
    args = parser.parse_args()
    """
    print(descStr)
    Radii, radii, l = getPlayerInput()
    ts.setup(width=0.8)
    myturtle.shape('turtle')
    ts.title('Spirographs')
    ts.onkey(saveDrawing, 's')
    ts.listen()
    myturtle.hideturtle()
    
    """
    if args.sparms:
        params = [float(x) for x in args.sparams]
        color = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, color, *params)
        spiro.draw()
    else:
        spiroAnim = SpiroAnimator(4)
        turtle.onkey(spiroAnim.toggleTurtles(), "t")
        turtle.onkey(spiroAnim.restart(), "space")
    """
    
    if Radii != None and radii != None and l != None:
        color = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, color, Radii, radii, l)
        spiro.draw()
    else:
        spiroAnim = SpiroAnimator(4)
        ts.onkey(spiroAnim.toggleTurtles(), "t")
        ts.onkey(spiroAnim.restart(), "space")
          
    ts.mainloop()
    
if __name__ == '__main__':
    main()
        
    
        

