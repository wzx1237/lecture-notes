# design an object
import turtle
class square:
    # must tab '__init__'
    def __init__(self,length,x,y):
        # store it inside object
        self.mylength=length
        self.x=x
        self.y=y
    # square
    def area(self):
        return self.mylength*self.mylength
    def draw(self):
        turtle.up()
        turtle.goto(self.x,self.y)
        turtle.down()
        for _ in range(4):
            turtle.forward(self.mylength)
            turtle.left(90)
# self is myself or itself
# so the first thing must be self
"""
x=square(4,0,50)
print("area is",x.area())
"""
# or you can use it like that:
"""
print("area is",square(4,0,50).area())
x.mylength=100
print("area is",x.area())
x.draw()
turtle.done()
"""


        
        
