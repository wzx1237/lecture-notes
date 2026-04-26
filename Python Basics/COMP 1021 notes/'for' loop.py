import turtle
# range function
print(range(1,6))
# the outcome is:
# range(1,6)
# to see the number returned:
print(list(range(1,6)))
# the output is:
# [1, 2, 3, 4, 5]

# also, there has advanced version
print(list(range(1,10,3)))
# the output is:
# [1, 4, 7]

# So, what is for loop?
"""
for item in a list of items:
    ...statements()...
"""
# the statements will be executed for each item
# some example:
for words in ['ant','tree','hello-world','fair']:
    print(words, end=" ")
# here end=" " means a space is put 
# at the end of the number when 
# it is printed, instead of going to 
# the next line

# the output is:
"""
ant tree hello-world fair 
"""

# another one:
print()
for word in ("yellow","ought","unbrella"):
    print(word[0], end="")
# the output is:
# you

# another one:
print()
for i in (1,0,9):
    print(i, end=", ")
# the output is:
# 1, 0, 9,



# a nest loop
row=0
while row<10:
    c=0
    while c<10:
        turtle.goto(c*10,row*10)
        turtle.dot(10)
        c=c+1
    row=row+1
turtle.done()
        
    
