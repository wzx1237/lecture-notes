import turtle
print('Welcome to the Python Sketchbook!')
print()
print('Please choose one of the following options:')
print()
print('m - Move the turtle')
print('t - Rotate the turtle')
print('l - Draw a line')
print('r - Draw a rectangle')
print('c - Draw a circle')
print('p - Change the pen colour of the turtle')
print('f - Change the fill colour of the turtle')
print('g - Draw a generated flower')
print('e - Draw a generated explosion')
print("a - Draw the author's information ")
print('q - Quit the program')
print()
decide=True  #loop 1
while decide :
    option=input('Please enter your option:')#decide your option
    if option=="m" :#move the turtle
        print()
        x=int(input('Please enter the x value: '))
        y=int(input('Please enter the y value: '))
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
    if option=="t" :#rotation the turtle
        print()
        angle=int(input('Please enter the angle of rotation'))
        turtle.left(angle)
    if option=="l" :#draw a line
        print()
        x=int(input('Please enter the x value: '))
        y=int(input('Please enter the x value: '))
        turtle.goto(x,y)
    if option=="r":#draw a rectangle
        print()
        x=int(input('Please enter the width of the rectangle: '))
        y=int(input('Please enter the height of the rectangle: '))
        loop=1
        turtle.begin_fill()
        while loop<=2 :
            turtle.forward(x)
            turtle.left(90)
            turtle.forward(y)
            turtle.left(90)
            loop=loop+1
        turtle.end_fill()
    if option=="c" :#draw a circle
        print()
        x=int(input('Please enter the diameter you want: '))
        turtle.begin_fill()
        turtle.circle(x)
        turtle.end_fill()
    if option=="p" :#change the pen color
        print()
        mycolor=input('Please enter a colour name for the pen colour: ')
        turtle.pencolor(mycolor)
    if option=="f" :#change the fill color
        print()
        my_fill_color=input('Please enter a colour name for the fill colour: ')
        turtle.fillcolor(my_fill_color)
    if option=="g" :#draw a flower(need not fill color)
        print()
        petal_size=int(input('Please enter the size of the flower petal: '))
        outer_loop=1
        while outer_loop<=12 :
            inner_loop=1
            while inner_loop<=3 :
                turtle.forward(petal_size)
                turtle.left(120)
                inner_loop=inner_loop+1
            turtle.left(30)
            outer_loop=outer_loop+1
    if option=="e" :#explosion
        size=int(input('Please enter the size of the explosion (>150): '))
        for color in ["sienna", "brown",  \
                  "red","orange","gold","yellow"]:
            for t in range (1,5) :
                mycolor=color + str(t)
                turtle.color(mycolor)
                turtle.dot(size)
                size=size-5
    if option=="a" :#write author's name
        turtle.up()#write W
        turtle.goto(-200,50)
        turtle.down()
        turtle.right(75)
        n=0
        while n<4 :
            turtle.forward(100)
            angle=((-1)**n)*150
            turtle.left(angle)
            n=n+1
        turtle.right(75)#finish W and redirect
        turtle.up()#write Z
        turtle.goto(0,50)
        turtle.down()
        turtle.goto(100,50)
        turtle.goto(0,-40)
        turtle.goto(100,-40)
        turtle.up()#write X
        turtle.goto(120,50)
        turtle.down()
        turtle.goto(200,-40)
        turtle.up()
        turtle.goto(200,50)
        turtle.down()
        turtle.goto(120,-40)
    if option=="q" :
        decide=False
turtle.done()
        
        
            
        
        
        
        
        


      
