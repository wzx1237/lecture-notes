import turtle
import random
x=random.randint(1,100)
b=0
y=0
a=True
while a :
    n=turtle.textinput("Guessing Game","guess a number between 1 and 100:")
    n_int=int(n)
    turtle.up()
    turtle.goto(0,y)
    y=y-30
    turtle.down()
    if n_int<x :
        turtle.write("your answer is "+ n +"it's lower")
        b=b+1
    elif n_int>x :
        turtle.write('your answer is '+ n +"it's higher")
        b=b+1
    elif n_int==x :
        a=False
turtle.write("Congratulation! you use"+ str(b) +"attempts to get the right answer")
turtle.done()
