#mine sweeper
import random
import turtle
import time

turtle.setworldcoordinates(0,0,100,100)
map=[[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]]
# 9 means mine
# 0 means no mine and no mine around it
# -1 means correctly marked mine
# mine_count means the number of mine in our game

mine_count=15
positions=[]
for i in range(10):
    for j in range(10):
        position=[i,j]
        positions.append(position)
# for check use:
"""
print(positions)
"""
positions.remove([0,0])# important code
for _ in range(mine_count):
    i=random.randint(0,len(positions)-1)
    mine_position=positions[i]
    map[mine_position[0]][mine_position[1]]=9
    positions.remove(positions[i])

# for check use:
"""
for item in map:
    print(item)
"""
# for check use:
"""
mine_num=0
for i in range(10):
    for j in range(10):
        if map[i][j]==9:
            mine_num+=1
print(mine_num)
"""
def square(x,y):
    turtle.up()
    turtle.goto(10*x,10*y)
    turtle.down()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

# count the mine number(around you)
def mine_around_you(a,b):
    count=0
    for i in range(max(a-1,0),min(a+2,10)):
        for j in range(max(b-1,0),min(b+2,10)):
            if map[i][j]==9 or map[i][j]==-1:
                count=count+1
    if count!=0:
        turtle.up()
        turtle.goto(10*b+4,10*(9-a)+4)
        turtle.down()
        turtle.write(count,font=("Arial", 20, "bold"))
    return count
def click_block_l(x,y):
    global row,col
    col,row=9-min(max(int((100-x)/10),0),9),9-min(max(int(y/10),0),9)
    # for check use:
    #print(row,col)
    turtle.onscreenclick(click_block_l)
def click_block_r(x,y):
    global marked_row,marked_col
    marked_col,marked_row=9-min(max(int((100-x)/10),0),9),9-min(max(int(y/10),0),9)
    # for check use:
    #print(marked_row,mark_col)
    turtle.onscreenclick(click_block_r)


def mark(a,b):
    turtle.tracer(False)
    turtle.up()
    if map[a][b]==9:
        map[a][b]=-1
    # for check use:
    # print(map)
    turtle.goto(10*b+5,10*(9-a)+6)
    turtle.down()
    
    # draw a red triangle to mark it
    
    turtle.right(120)
    turtle.width(1)
    turtle.fillcolor("red")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(3)
        turtle.left(120)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.tracer(True)

def choose_mark():
    global mark_state
    mark_state=True
    turtle.onkeypress(choose_mark,"m")
def not_choose_mark():
    global mark_state
    mark_state=False
    turtle.onkeypress(not_choose_mark,"n")
def open_lot_block(row,col,recursion):
    if map[row][col] != -1 and map[row][col] != 9:
        square(col,9-row)
        around_mine_num=mine_around_you(row,col)
    # advanced version:
    
    if recursion>3:
        return
    elif recursion<=3 and around_mine_num==0 :
        open_lot_block(min(row+1,9),col,recursion+1)
        open_lot_block(max(row-1,0),col,recursion+1)
        open_lot_block(row,min(col+1,9),recursion+1)
        open_lot_block(row,max(col-1,0),recursion+1)

def mark_correctly():
    num=0
    for i in range(10):
        num+=map[i].count(-1)
    if num==mine_count:
        return True
    elif num!=mine_count:
        print("you must get something wrong!")
        return False
    
#############################
# start our mainloop
turtle.width(5)
turtle.speed(0)
turtle.fillcolor("blue")
turtle.tracer(False)
for i in range(10):
    for j in range(10):
        square(i,j)
turtle.tracer(True)

start=True
a=time.time()

marked_row,marked_col=11,11
row,col=0,0
turtle.listen()

click_count=0
mark_state=False
while start and click_count<=mine_count:
    # btn=1表示鼠标左键
    # btn=2表示鼠标右键,but it doesn't work
    turtle.onkeypress(choose_mark,"m")
    turtle.onkeypress(not_choose_mark,"n")
    # for check use:
    #print(mark_state)
    # because we can't use right mouse button
    # we use keyboard to control it
    # button 'm'+click == right click in original minesweeper
    # button 'n'+click == left  click in original minesweeper
    if not mark_state:
        turtle.onscreenclick(click_block_l)
    else:
        turtle.onscreenclick(click_block_r)   
    if map[row][col]==9 or map[row][col]==-1:
        turtle.up()
        turtle.goto(25,50)
        turtle.down()
        turtle.write("Oh, No! You lose!",font=("Arial", 20, "bold"))
        start=False       
    else:
        if marked_row!=11 and marked_col!=11:
            mark(marked_row,marked_col)
            # advanced version:
            
            if click_count<=mine_count-1:
                click_count+=1
            elif click_count==mine_count:
                judge=mark_correctly()
                if judge:
                    start=False
                else:
                    start=True
            
            #original one:
            #click_count=click_count+1
            marked_row,marked_col=11,11
        if map[row][col]!=9:
            turtle.tracer(False)
            turtle.width(5)
            turtle.fillcolor("white")
            open_lot_block(row,col,0)
            turtle.tracer(True)
            
b=time.time()
turtle.up()
turtle.goto(25,25)
turtle.write("Game Finished",font=("Arial", 20, "bold"))
turtle.goto(25,0)
turtle.write("You used:"+str(b-a)+" seconds",font=("Arial", 20, "bold"))


turtle.done()      
