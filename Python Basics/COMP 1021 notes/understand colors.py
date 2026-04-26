# understanding colors
import turtle
# turtle调色
turtle.colormode(255)
# Here:
# black (0,0,0)     white (255,255,255)
# red   (255,0,0)   green (0,255,0)
# blue  (0,0,255)   gray  (127,127,127)
# yellow(255,255,0) Cyan  (0,255,255)
# magenta(255,255,0)
turtle.setworldcoordinates(0,0,4,255)
turtle.hideturtle()
# create new turtle
# red one
red=turtle.Turtle()
red.up()
red.fillcolor("red")
red.shape("square")
red.shapesize(3,8)
red.speed(0)
red.goto(1,0)
red.left(90)
# green one
green=turtle.Turtle()
green.up()
green.fillcolor("green")
green.shape("square")
green.shapesize(3,8)
green.speed(0)
green.goto(2,0)
green.left(90)
# blue one
blue=turtle.Turtle()
blue.up()
blue.fillcolor("blue")
blue.shape("square")
blue.shapesize(3,8)
blue.speed(0)
blue.goto(3,0)
blue.left(90)

def red_ondrag(x,y):
    # ignore any dragging
    red.ondrag(None)
    red.goto(1,y)
    update_bg_color()
    # handle any dragging once again
    red.ondrag(red_ondrag)
def green_ondrag(x,y):
    # ignore any dragging
    green.ondrag(None)
    green.goto(2,y)
    update_bg_color()
    # handle any dragging once again
    green.ondrag(green_ondrag)
def blue_ondrag(x,y):
    # ignore any dragging
    blue.ondrag(None)
    blue.goto(3,y)
    update_bg_color()
    # handle any dragging once again
    blue.ondrag(blue_ondrag)
def update_bg_color():
    red_number=max(min(red.ycor(),255),0)
    green_number=max(min(green.ycor(),255),0)
    blue_number=max(min(blue.ycor(),255),0)
    print(int(red_number),int(green_number),int(blue_number))
    turtle.bgcolor(int(red_number),int(green_number),int(blue_number))
red.ondrag(red_ondrag)
green.ondrag(green_ondrag)
blue.ondrag(blue_ondrag)

turtle.done()
