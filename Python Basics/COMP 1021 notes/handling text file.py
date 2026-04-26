# 11.8 handling text file
import turtle
"""
orchid=turtle.Turtle()
red=turtle.Turtle()
orange=turtle.Turtle()
"""
# tab

thing1 = "\t" # a tab
# a special way to tab 1 thing
# len(thing1)=1
"""
print("okok\tbuuu\tyaaaa\thhaa\tsgugu")
"""
# the outcome is:
# okok	buuu	yaaaa	hhaa	sgugu
"""
for x in range(5):
    print("\t"*x+"hello")
"""
#########################
thing2 = "\n"# end of line character
"""
print("okok\nhjhh\njjxx\nfgytfyf\nj")
"""
# the outcome is:
"""
okok
hjhh
jjxx
fgytfyf
j
"""
# example
"""
for x in range(5):
    print("hello"+"\n"*x, end="")
"""
# the outcome is:
"""
hellohello
hello

hello


hello




"""
# example
"""
for x in range(50):
    print(x, end="- ")# 加上end=""后可以让结果不换行
"""
# split and rstrip
line="trump,like,burger"
# split 可以让text从特定位置断开，并把它变成list
# rstrip 可以去掉换行
#####################
def save():
    filename=turtle.textinput("Save",\
                              "what is the file name you want to save?")
    # 创建我们的存档，并打开它 for writing
    myfile=open(filename,"wt")
    for this_turtle in allturtle:
        # 生成我们的存档
        one_line=str(this_turtle.xcor())+"\t"+\
                  str(this_turtle.ycor())+"\n"
        # 写进存档
        myfile.write(one_line)
    myfile.close()
def load():
    filename=turtle.textinput("load","what is the file name you want to save?")
    # open our file for reading
    myfile=open(filename,"r")
    index=0
    for line in myfile:
        # remove the end-of-line
        line=line.rstrip()
        # seperate the two items
        items=line.split("\t")
        x=float(item[0])
        y=float(item[1])
        allturtle[index].goto(x,y)
        index=index+1
    myfile.close() # finished it and close it

# some tips:
"""
we can use: line=line.rstrip().split("\t")
to replace: "line=line.rstrip()"
            "line=line.split("\t")"
And we can use split(" ")
to break the sentences into words
"""
# like that:
sentence="The men can be seeing firing guns in the air in \
celebration on the otherwise deserted entrance area"
words=sentence.split(" ")
print(words)
# the output:
"""
['The', 'men', 'can', 'be', 'seeing', 'firing', 'guns',\
'in', 'the', 'air', 'in', 'celebration',\
'on', 'the', 'otherwise', 'deserted', 'entrance', 'area']
"""
