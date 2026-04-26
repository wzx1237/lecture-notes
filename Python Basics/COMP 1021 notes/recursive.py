# repeating pattern
# recursive depths:

count=0
def fun(x):
    global count
    print(x)
    if x<4:
        fun(x+1)
    count=count+1
fun(0)

#the oucome:
"""
0
1
2
3
4
"""
def print_0_4(n):
    print(n)
    if n<4:
        print_0_4(n+1)
print_0_4(0)
# the output is:
"""
0
1
2
3
4
"""
# what will happen when we change the order?
def print_4_0(n):
    if n<4:
        print_4_0(n+1)
    print(n)
print_4_0(0)
# output:
"""
4
3
2
1
0
"""


"""
def re(n):
    if n==1:
        return 1
    else:
        return re(n-1)*n
x=re(3)
print(x)
"""
# the answer is 6
# 这是一个计算阶乘的方法

# 例子
c=0
def show(x, maxdepth):
    global c
    c=c+1
    if x < maxdepth:
        show(x+1, maxdepth)
        show(x+1, maxdepth)
        show(x+1, maxdepth)
show(0,10)
print(c)
# outcome
# 88573
c=0
def show(x, maxdepth):
    global c
    if x < maxdepth:
        show(x+1, maxdepth)
        show(x+1, maxdepth)
        show(x+1, maxdepth)
    c=c+1
show(0,10)
print(c)
# outcome
# 88573
c=0
def show(x, maxdepth):
    global c
    if x>=maxdepth:
        return
    elif x < maxdepth:
        show(x+1, maxdepth)
        show(x+1, maxdepth)
        show(x+1, maxdepth)
    c=c+1
show(0,10)
print(c)
# output
# 29524
