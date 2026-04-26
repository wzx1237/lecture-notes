import turtle
import random
# another way to say:"turtle.done()"=="turtle.mainloop()"

# all turtrle objects have this:
# varibles (often called 'attributes' or 'properties')
# function (often called 'method')

# how to control lots of turtles

allturtle=[]
turtle.hideturtle()
def create_turtle(color):
    thisturtle=turtle.Turtle()
    thisturtle.fillcolor(color)
    thisturtle.up()
    thisturtle.shape("turtle")
    thisturtle.shapesize(2,2)
    
    thisturtle.goto(random.randint(-10,10),random.randint(-20,20))
    
    allturtle.append(thisturtle)# add my turtle in the list
def change_one_turtle():
    index=random.randint(0,int(len(allturtle)-1))
    allturtle[index].left(random.randint(-90,90))
    allturtle[index].forward(20)
#######
#######
# main loop
create_turtle("red")
create_turtle("green")
create_turtle("purple")
create_turtle("yellow")
while True:
    change_one_turtle()
turtle.done()

# 拼贴画
# see example 5
