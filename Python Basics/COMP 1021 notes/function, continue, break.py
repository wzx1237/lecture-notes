#创建记事簿
"""
list=[]
print('start to create your note book!')
print('if you want to create a note, tab add and if you finish it, tab finish')
option=""
while option != "finish" :
    daily_task=input("what's your daily task?")
    option=input('input your chioce')
    list.append(daily_task)
else:
    print('')
while list != [] :
    finished_task=input('which task have you finished?')
    list.remove(finished_task)
    print(list,'that is your task.')
else :
    print('good job! you have finished all of your daily task.')
"""
#关于if 语句判断的简省
"""
x=5
if x :
    print("ok")
if 0 :
    print("no")
"""
# 'i%2 != 0' is the same as 'i%2'

#函数
"""
import turtle
size=int(input('choose a size'))
angle=int(input('choose a angle'))
turtle.speed(0)
def spiral(size,angle):
    for i in range (2,size,4):
        turtle.forward(i)
        turtle.left(angle)
spiral(size,angle)
"""

#break and continue
# continue说明要跳过这个事件并继续loop
"""
for i in range (1,100):
    if i == 4:
        continue#跳过这个数/事件
    if i == 10:
        break
    print(i)
"""
# the continue command:
# stops the 'current'execution of the loop
# the break command:
# stops the whole execution of the loop
for i in range(10):
    print(i)
    if i==9:
        break
    if i%4==0:
        continue
    print(i)
# output:
"""
0
1
1
2
2
3
3
4
5
5
6
6
7
7
8
9
"""
# example:
# draw a chess board:
import turtle
turtle.speed(8)
for i in range(8):
    for j in range(8):
        if i%2 == j%2:
            turtle.up()
            turtle.goto(20*j,20*i)
            turtle.down()
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(20)
                turtle.left(90)
            turtle.end_fill()
turtle.done()
