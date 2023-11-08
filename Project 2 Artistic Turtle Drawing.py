import turtle 

wn = turtle.Screen()
wn.bgcolor("sky blue")
pen = turtle.Turtle() 
pen.speed(0)
pen.shape("blank")

############################################# BACKGROUND #############################################

def coordinates(t, x, y):
    """
    Function to move turtle pen to different locations.
    """
    t.up()
    t.goto(x, y)
    t.down()

def grass(t, length, width):
    """
    Function to draw grass at the bottom of the screen in the color light green.
    """
    t.color("lightgreen")
    t.begin_fill()
    exterior_angle = 360 / 4 
    for _ in range(2):
        t.forward(length)
        t.right(exterior_angle)
        t.forward(width)
        t.right(exterior_angle)
    t.end_fill()

############################################# FLOWER POT #############################################

def pot(t, side_1, side_2):
    """
    Function to draw a flower pot shaped as an isosceles trapezoid, in the color sienna.
    """
    t.color("sienna")
    t.begin_fill()
    t.forward(side_1)
    t.right(120)
    for _ in range(3):
        angle = 360 / 6 
        t.forward(side_2)
        t.right(angle)
    t.end_fill()


############################################# FLOWER STEM #############################################

def stem(t, length):
    """
    Function to draw a flower stem, in the color forest green.
    """
    t.color("forest green")
    t.pensize(5)
    t.forward(length)
    t.up()
    t.backward(length)
    t.down()

############################################# FLOWER 1 #############################################


def flower_petal(t, radius):
    """
    Function to draw a singular flower petal.
    """
    for _ in range(2):
        t.circle(radius, 60)
        t.left(120)

def flower_basic(t, petal_radius, num_petals):
    """
    Function to draw a flower with num_petals number of petals.
    """
    for _ in range(num_petals):
        flower_petal(t, petal_radius)
        t.right(360 / num_petals)

############################################# FLOWER 2 #############################################

def flower_with_pattern(t, num_petals, initial_radius, increasing_radius_amount):
    """
    Function to draw multiple flower petals, each increasing in size and rotating at an angle. 
    """
    for i in range(num_petals):
        radius = initial_radius + i * increasing_radius_amount
        flower_petal(t, radius)
        t.right(360 / num_petals)

############################################# FLOWER 3 #############################################

def circle(t, radius): 
    """
    Function to draw a circle.
    """
    t.circle(radius)

def circle_flower(t, flower_radius):
    """
    Function to draw a circular flower
    """
    for _ in range(flower_radius):
        circle(t, flower_radius)
        pen.left(360 / flower_radius)
    

##########################################################################################

### draw grass
coordinates(pen, -360, -100)
grass(pen, 720, 250)

### draw flower pot
coordinates(pen, -200,-50)
pot(pen, 400,200)

### draw a basic flower
coordinates(pen, 0, 150)
pen.right(150)
stem(pen, 200)

pen.color("deep pink")
pen.pensize(1)
pen.begin_fill()
flower_basic(pen, 75, 12)
pen.end_fill()

### draw a flower with increasing petal sizes
coordinates(pen, -125, 50)
stem(pen, 100)

pen.color("medium orchid")
pen.pensize(1)

for _ in range(6):
    flower_with_pattern(pen, 12, 2, 4)
    pen.right(360 / 6)

### draw a circular flower
coordinates(pen, 125, 50)
stem(pen, 100)

pen.color("yellow")
pen.pensize(1)
circle_flower(pen, 20)


### Drawing is complete
wn.exitonclick()


