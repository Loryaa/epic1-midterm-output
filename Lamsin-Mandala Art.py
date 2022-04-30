import turtle
turtle.title(titlestring="Mandala Art - Lamsin")

# Turtle for Circle
crc = turtle.Turtle()
crc.speed(0)

# Turtle for Partition
pt = turtle.Turtle()
pt.speed(0)

# Turtle for Lines
ln = turtle.Turtle()
ln.speed(0)

# Screen
scr = turtle.Screen()
scr.bgcolor('black')
scr.setup(width=1.0, height=1.0)

# Classes
class Colors():
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

class PenSize():
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

# Objects
clr = Colors('black', 'white', '#d4d4d4', '#fff01f')
ps = PenSize(1, 3, 5, 10)

# Functions
def drawSpiral():
    for i in range(650):
        turtle.forward(i)
        turtle.left(91)

def filled(r, e):
    crc.begin_fill()
    crc.circle(r, e)
    crc.end_fill()

def PosCrc(a, b):
    crc.pu()
    crc.setpos(a, b)
    crc.pd()

def drawline(angle):
    pt.left(angle)
    pt.forward(200)

def drawpartition():
    drawline(22.5)
    for i in range(7):
        pt.pu()
        pt.setpos(0, 0)
        pt.pd()
        drawline(45)

def LinePos(x, y):
    ln.pu()
    ln.setpos(x, y)
    ln.pd()

def patterline(angle, length, draw):
    LinePos(0, 0)
    ln.left(angle)
    ln.pu()
    ln.forward(length)
    ln.pd()
    ln.forward(draw)

# Drawing Square-Spiral
turtle.speed(0)
turtle.pensize(ps.s1)
turtle.color(clr.c4)
drawSpiral()

# Pattern Circles
PosCrc(0, 203)
crc.color(clr.c3, clr.c3)
filled(-203, 360)
PosCrc(0, 183)
crc.color(clr.c1, clr.c1)
filled(-183, 360)
PosCrc(0, 163)
crc.color(clr.c3, clr.c3)
filled(-163, 360)
PosCrc(0, 160)
crc.color(clr.c1, clr.c1)
filled(-160, 360)
crc.pensize(ps.s2)
crc.color(clr.c3)
PosCrc(0, 140)
crc.circle(-140)
PosCrc(0, 120)
filled(-120, 360)
crc.pensize(ps.s2)
PosCrc(0, 203)
crc.color(clr.c2)
crc.circle(-203)

# Partitions
pt.color(clr.c3)
pt.pensize(ps.s4)
drawpartition()

# Pattern for Lines
ln.color(clr.c3)
ln.pensize(ps.s3)
LinePos(0, 100)
ln.left(90)
ln.forward(100)
patterline(45, 140, 45)
patterline(45, 120, 20)
ln.pu()
ln.forward(21)
ln.pd()
ln.forward(20)
patterline(45, 162, 20)
patterline(90, 120, 18)
patterline(45, 140, 18)
patterline(45, 120, 42)

# Yin Yang Design
PosCrc(0, 100)
crc.color(clr.c1, clr.c1)
filled(-100, 180)
PosCrc(0, 100)
crc.color(clr.c3, clr.c3)
filled(100, 180)
filled(50, 360)
PosCrc(0, 0)
crc.color(clr.c1, clr.c1)
filled(50, 360)
PosCrc(0, -70)
filled(20, 360)
PosCrc(0, 30)
crc.color(clr.c3, clr.c3)
filled(20, 360)
PosCrc(0, 100)
crc.pensize(ps.s2)
crc.color(clr.c2)
crc.circle(-100)

turtle.ht()
crc.ht()
pt.ht()
ln.ht()

turtle.done()
input()