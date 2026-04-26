import random
import turtle
n=int(input("how many circles do you want?"))
b=1
turtle.up()
turtle.width(8)
turtle.speed(8)
list1=["red",'blue','green','yellow','purple','pink','black']
while b>=1 and b<= (n-1) :
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    z=random.randint(1,80)
    e=random.choice(list1)#如何随机选择
    a=random.choice(list1)
    turtle.fillcolor(a)#fill a random color
    turtle.pencolor(e)#randomly decided pencolor
    turtle.goto(x,y)
    #randomly choose a place and draw a circle
    turtle.begin_fill()
    turtle.down()
    turtle.circle(z)
    turtle.end_fill()
    turtle.up()
    b=b+1
else:
    print("finished")
