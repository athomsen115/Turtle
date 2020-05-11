import turtle, math, argparse

def genThueMorse():
    tms = '0'
    curr = 0
    while True:
        if curr == len(tms):
            tmp = ''
            for i in range(len(tms)):
                if tms[i] is '0':
                    tmp += '1'
                else:
                    tmp +='0'
            tms += tmp
        yield tms[curr]
        curr += 1

def drawThueMorse(x, y):
    turt = turtle.Turtle()
    turt.color('purple')
    turt.hideturtle()
    turt.up()
    turt.setpos(x, y)
    turt.down()
    tms = genThueMorse()
    delta = 4
    while True:
        a = next(tms)
        if a is '0':
            turt.fd(delta)
        else:
            turt.left(60)   

def kochSnowflake(x1, y1, x2, y2, turt):
    d = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    r = d/3.0
    h = r*math.sqrt(3)/2.0
    p3 = ((x1 + 2*x2)/3.0, (y1 + 2*y2)/3.0)
    p1 = ((2*x1 + x2)/3.0, (2*y1 + y2)/3.0)
    c = (0.5*(x1+x2), 0.5*(y1+y2))
    n = ((y1-y2)/2, (x2-x1)/d)
    p2 = (c[0]+h*n[0], c[1]+h*n[1])
    if d> 10:
        #flake 1
        kochSnowflake(x1, y1, p1[0], p1[1], turt)
        #flake 2
        kochSnowflake(p1[0], p1[1], p2[0], p2[1], turt)
        #flake 3
        kochSnowflake(p2[0], p2[1], p3[0], p3[1], turt)
        #flake 4
        kochSnowflake(p3[0], p3[1], x2, y2, turt)
        
    else:
        turt.up()
        turt.setpos(p1[0], p1[1])
        turt.down()
        turt.setpos(p2[0], p2[1])
        turt.setpos(p3[0], p3[1])
        turt.up()
        turt.setpos(x1, y1)
        turt.down()
        turt.setpos(p1[0], p1[1])
        turt.up()
        turt.setpos(p3[0], p3[1])
        turt.down()
        turt.setpos(x2, y2)

def drawkochSnow(x1, y1, x2, y2):
    turt = turtle.Turtle()
    turt.speed("fastest")
    turt.color('blue')
    turt.hideturtle()
    kochSnowflake(x1, y1, x2, y2, turt)

def main():
    decState = """
    This program draws the Koch Snowflake, which uses fractal geometry.
    The Koch Snowflake also has a deeper connection with the Thue-Morse sequence
    The program with no input generates the Koch Snowflake,
    with the input of 'thue', it generates the Thue-Morse sequence.
    Run both and check out the similarities
    """
    print(decState)
    """
    parser = argparse.ArgumentParser(description="Koch Snowflake")
    parser.add_argument('--thue', action='store_true', required=False)
    args = parser.parse_args()
    
    if args.thue:
        drawThueMorse(200, 200)
    else:
        drawkochSnow(-100, 0, 100, 0)
        drawkochSnow(0, -173.2, -100, 0)
        drawkochSnow(100, 0, 0, -173.2)
        win = turtle.Screen()
        win.exitonclick()
    """
    while True:
        thue = input("Press 'enter' to run the Koch Snowflake, or type 'thue' to see the Thue-Morse Sequence: ")
        if thue == '':
            win = turtle.Screen()
            drawkochSnow(-100, 0, 100, 0)
            drawkochSnow(0, -173.2, -100, 0)
            drawkochSnow(100, 0, 0, -173.2)
            win.exitonclick()
        elif thue.lower() == 'thue':
            drawThueMorse(200, 200)
        else:
            print("That was not a valid entry")
        
if __name__ == '__main__':
    main()