import turtle

# setting the window
win = turtle.Screen()
win_width = win.window_width()
win_height = win.window_height()
win.title('Painter')

turtle.tracer(0)

size = 5

left_border = turtle.Turtle('square')
left_border.color('#e7eae5')
left_border.shapesize(50)
left_border.speed(0)
left_border.pensize(5)
left_border.penup()
left_border.goto(-1180, 0)

right_border = turtle.Turtle('square')
right_border.color('#e7eae5')
right_border.shapesize(50)
right_border.speed(0)
right_border.pensize(5)
right_border.penup()
right_border.goto(1180, 0)

# setting arrows to increase and decrease the size of brush
increase = turtle.Turtle('triangle')
decrease = turtle.Turtle('triangle')
increase.penup()
decrease.penup()
increase.setheading(90)
decrease.setheading(270)
increase.goto(725, 300)
decrease.goto(725, 250)
increase.shapesize(2)
decrease.shapesize(2)

def increase_brush(x, y):
    global size
    size += 2

def decrease_brush(x, y):
    global size
    if size > 2 :
        size -= 2

# setting the brush
brush = turtle.Turtle()
brush.width(5)
brush.speed(0)
brush.shape('circle')
brush.shapesize(0.75)
brush.color('black')

# setting anti brush
anti = turtle.Turtle()
anti.width(5)
anti.speed(0)
anti.shape('circle')
anti.shapesize(0.75)
anti.color('black')

# go to this pos
brush.penup()
brush.goto(0, 0)
brush.pendown()
anti.penup()
anti.goto(0, 0)
anti.pendown()

def move(x, y):
    if x > -675 and x < 675:
        anti.goto(-x, y)
        brush.goto(x, y)


flag = 0
copy = 0

def find(x, y):
    if x > -675 and x < 675:
        anti.penup()
        anti.goto(-x, y)
        brush.penup()
        global cnt
        if cnt % 2 == 0:
            anti.pendown()
        brush.goto(x, y)
        brush.pendown()


def clear():
    anti.goto(0, 0)
    brush.goto(0, 0)
    anti.clear()
    brush.clear()

def erase(x, y):
    brush.shape('square')
    anti.shape('square')
    brush.color('grey')
    anti.color('grey')
    brush.pencolor('white')
    anti.pencolor('white')
    brush.pensize(size)
    anti.pensize(size)

# eraser border
eraser_border = turtle.Turtle('square')
eraser_border.penup()
eraser_border.goto(725, -300)
eraser_border.shapesize(2.5)
eraser_border.color('black')

# eraser
eraser = turtle.Turtle('square')
eraser.penup()
eraser.goto(725, -300)
eraser.shapesize(2)
eraser.color('grey')

# anti on off button
anti_on_off_border = turtle.Turtle('circle')
anti_on_off_border.shapesize(2.5)
anti_on_off_border.penup()
anti_on_off_border.goto(725, 0)
anti_on_off_border.color('#008000')

anti_on_off = turtle.Turtle('circle')
anti_on_off.shapesize(2)
anti_on_off.penup()
anti_on_off.goto(725, 0)
anti_on_off.color('#00ff00')

cnt = 0
def on_off(x, y):
    global cnt
    cnt += 1
    if cnt % 2 != 0:
        anti.hideturtle()
        anti.penup()
        anti_on_off.color('red')
        anti_on_off_border.color('dark red')
    else:
        anti.showturtle()
        anti.pendown()
        anti_on_off_border.color('#008000')
        anti_on_off.color('#00ff00')


# creating a palette
red = turtle.Turtle('square')
blue = turtle.Turtle('square')
green = turtle.Turtle('square')
yellow = turtle.Turtle('square')
purple = turtle.Turtle('square')
orange = turtle.Turtle('square')
pink = turtle.Turtle('square')
black = turtle.Turtle('square')
lime = turtle.Turtle('square')
cyan = turtle.Turtle('square')
brown = turtle.Turtle('square')
dark_blue = turtle.Turtle('square')
grey = turtle.Turtle('square')
raspberry = turtle.Turtle('square')
mango = turtle.Turtle('square')

# palette size
red.turtlesize(2)
orange.turtlesize(2)
yellow.turtlesize(2)
green.turtlesize(2)
blue.turtlesize(2)
purple.turtlesize(2)
pink.turtlesize(2)
black.turtlesize(2)
lime.turtlesize(2)
cyan.turtlesize(2)
brown.turtlesize(2)
dark_blue.turtlesize(2)
grey.turtlesize(2)
raspberry.turtlesize(2)
mango.turtlesize(2)

# palette, please don't make noise
red.penup()
orange.penup()
yellow.penup()
green.penup()
blue.penup()
purple.penup()
pink.penup()
black.penup()
lime.penup()
cyan.penup()
brown.penup()
dark_blue.penup()
grey.penup()
raspberry.penup()
mango.penup()

# palette colors
red.color('red')
orange.color('orange')
yellow.color('yellow')
green.color('#009e49')
blue.color('blue')
purple.color('purple')
pink.color('#f31ded')
black.color('black')
lime.color('lime')
cyan.color('cyan')
brown.color('brown')
dark_blue.color('dark blue')
grey.color('grey')
raspberry.color('#fa4f96')
mango.color('#ffc933')

# palette position
pink.goto(-725, 350)
red.goto(-725, 300)
orange.goto(-725, 250)
green.goto(-725, 200)
blue.goto(-725, 150)
black.goto(-725, 100)
yellow.goto(-725, 50)
purple.goto(-725, 0)
lime.goto(-725, -50)
cyan.goto(-725, -100)
brown.goto(-725, -150)
dark_blue.goto(-725, -200)
grey.goto(-725, -250)
raspberry.goto(-725, -300)
mango.goto(-725, -350)

def color_red(x, y):
    brush.shape('circle')
    anti.shape('circle')
    brush.color('red')
    anti.color('red')
    brush.pensize(size)
    anti.pensize(size)

def color_orange(x, y):
    brush.color('orange')
    anti.color('orange')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_yellow(x, y):
    brush.color('yellow')
    anti.color('yellow')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(5)
    anti.pensize(5)

def color_blue(x, y):
    brush.color('blue')
    anti.color('blue')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_green(x, y):
    brush.color('#009e49')
    anti.color('#009e49')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_pink(x, y):
    brush.color('#f31ded')
    anti.color('#f31ded')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_purple(x, y):
    brush.color('purple')
    anti.color('purple')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_black(x, y):
    brush.color('black')
    anti.color('black')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_brown(x, y):
    brush.color('brown')
    anti.color('brown')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_cyan(x, y):
    brush.color('cyan')
    anti.color('cyan')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_lime(x, y):
    brush.color('lime')
    anti.color('lime')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_dark_blue(x, y):
    brush.color('dark blue')
    anti.color('dark blue')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_grey(x, y):
    brush.color('grey')
    anti.color('grey')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_raspberry(x, y):
    brush.color('#fa4f96')
    anti.color('#fa4f96')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

def color_mango(x, y):
    brush.color('#ffc933')
    anti.color('#ffc933')
    brush.shape('circle')
    anti.shape('circle')
    brush.pensize(size)
    anti.pensize(size)

while True:
    turtle.update()

    # moving mouse
    brush.ondrag(move)
    anti.ondrag(move)

    brush.pensize(size)
    anti.pensize(size)

    # listen
    turtle.listen()
    # turtle.onkey(clear, 'c')

    anti_on_off.onclick(on_off)

    turtle.onkey(clear, 'c')

    eraser.onclick(erase)

    increase.onclick(increase_brush)
    decrease.onclick(decrease_brush)

    win.onclick(find)

    red.onclick(color_red)
    orange.onclick(color_orange)
    yellow.onclick(color_yellow)
    green.onclick(color_green)
    blue.onclick(color_blue)
    purple.onclick(color_purple)
    pink.onclick(color_pink)
    black.onclick(color_black)
    lime.onclick(color_lime)
    cyan.onclick(color_cyan)
    brown.onclick(color_brown)
    dark_blue.onclick(color_dark_blue)
    grey.onclick(color_grey)
    raspberry.onclick(color_raspberry)
    mango.onclick(color_mango)

turtle.done()
