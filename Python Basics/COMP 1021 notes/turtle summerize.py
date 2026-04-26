import turtle
# notes on turtle

# zero: set world coordinates
turtle.setworldcoordinates(0,0,100,100)



# first: basic movement
turtle.forward(50)
turtle.goto(100,100)
# turtle will go to (100,100)
turtle.left(90)
# turtle will left 90 degrees
turtle.right(60)
# turtle will right 60 degrees
turtle.home()
# turtle will back to (0,0)



# second: drawing
turtle.up()
turtle.goto(50,50)
# 即使turtle.up()也能够dot
turtle.dot(50)
turtle.down()
# turtle will draw a black dot with diameter 50
# even when turtle is up, it also can draw a dot.
turtle.clear()
# it will clear what 'this' turtle drew,
# but do not affect others
turtle.circle(30,90)
# draw a quarter of circle with radius 30



# third: turtle_setting
turtle.colormode(255)
# adjust the color mode
# e.x.
"""
(0,0,0) is white
(255,0,0) is red
(0,255,0) is blue
(0,0,255) is green
"""
turtle.bgcolor(0,0,255)
# create a new turtle, called dog
dog=turtle.Turtle()
dog.color((0,0,0),(0,255,0))
"""
that equals to 'dog.pencolor('white')'
               'dog.fillcolor('blue')'
also, we note that:
    "turtle.color("red")" == "pencolor=red and fillcolor=red"
"""
x=turtle.xcor()
# return the x position of the turtle
y=turtle.xcor()
# return the y position of the turtle
h=turtle.heading()
# return the angle od the turtle, in degrees
pc,fc=turtle.pencolor(),turtle.fillcolor
# return the pencolor and fillcolor of the turtle
w=turtle.width()
# return the width of the turtle line




# forth: writing and input
# 即使在turtle.up()的状态下，turtle.write()
# 也能正常运行
"""
turtle.write("TEXT",font=("FONTYPE",FONTSIZE,"FONTSTYLE"))
"""
"""
turtle.input("title","prompt")
"""
# turtle.write can only write text/number
turtle.up()
# it can't write like that:
# turtle.write("just like 1+1 is",1+1,"my heart for you is",True)
# but you can do this:
turtle.write("just like 1+1 is"+str(1+1)+"my heart for you is"+str(True))
