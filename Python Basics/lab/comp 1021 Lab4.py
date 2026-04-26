import turtle
import time
import random
import playsound


screen_width, screen_height = 900, 564
firework_radius=100  #烟花最大半径
firework_count=30    #烟花数量
firework_colours=['red','orange','yellow',\
                  'green','cyan','blue','violet',\
                  'gold','white']
###设置背景
turtle.setup(screen_width,screen_height)
turtle.bgpic('hug.png')##set up your background
###设置turtle
turtle.width(3)
turtle.shape('circle')#change the shape of our turtle
turtle.color('red')
turtle.setheading(0)
for i in range(firework_count):
    #clear the sky for every 5 firework
    if i>0 and i%5 ==0:
        time.sleep(1)
        turtle.clear()
    ###设定初始值
    initial_y=-(screen_height/2)
    initial_x=random.randint(-450,450)
    initial_x=int(initial_x)
    turtle.up()
    turtle.goto(initial_x,initial_y)
    ###final position
    final_x=random.randint(-450,450)
    final_y=random.randint(0,282)
    turtle.goto(final_x,final_y)
    ###exploding the firework
    """first:choose the color of your firework"""
    color=firework_colours[random.randint(0,(len(firework_colours)-1))]
    turtle.color(color)
    firework_size=random.randint(45,firework_radius)
    turtle.setheading(0)#调整turtle指的方向
    ###添加音效
    playsound.play("explosion.wav")
    #initial_radius=10
    """second: exploding"""
    for r in range (10, firework_size,10):
        #move our center to produce the 'gravity'effect
        center_down=3
        #temporarily stop updating the diplay
        turtle.tracer(False)
        #准备
        turtle.forward(r)
        turtle.left(90)
        turtle.down()
        dot_radius=3
        #开始描点
        for dots in range(12):
            turtle.dot(dot_radius)
            turtle.up()
            turtle.circle(r,30)
            turtle.down()
        #adjust the dot size
        if dot_radius <=5 :
            dot_radius=dot_radius+5
        elif dot_radius>=30 :
            dot_radius=30
        #开始移动中心，产生重力效果
        turtle.up()
        #这里center_down=3
        final_y=final_y-center_down
        turtle.goto(final_x,final_y)
        turtle.setheading(0)
        #update the display
        turtle.tracer(True)
    turtle.hideturtle()
turtle.done()       




        
