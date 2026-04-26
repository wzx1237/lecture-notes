###
### this is an example about how to use elif
"""
for i in range(10):
    if i==1:
        print('ok')
    elif i==4:
        print('thank you')
    elif i==5:
        continue
    elif i==9:
        print(1)
"""
### this is an example about how to use elif
"""
count=0
while count<= 9 :
    count=count+1
    if count==1:
        print('ok')
    elif count==1 and True :
        print('reach 1')
    elif count==4:
        print('thank you')
    
    elif count==5:
        continue
    elif count==5:
        print('reach 5')
    elif count==9:
        print(1)
    print('how may?')
"""  
#today's lecture: function return
"""
def double(my_money):
    # this money is a local varible
    my_money = my_money * 2
    #so if you want got result, you need to use return
    return my_money
#main part
money = int(input('your money'))
print(money)
money= double(money)
print(money)
"""
# or you can use 'global'
"""
def double(money):
    # this money is a local varible
    global money
    #we can use global to make those two money be the same one 
    money = money * 2
    
#main part
money = int(input('your money'))
print(money)
money= double(money)
print(money)
"""
### data's category

#number: integer/float
a=50
f=40.97
#string
b="Hi"
#boolean: such as True/False
c=True
#list
d=[]
#tuple
e=(9,7)
# we can use "type" to find what type varible is
"""
list1=[a,b,c,d,e,f]
for i in list1 :
    if type(i) == int or type(i) == float :
       print(type(i))
"""
# we can use type in our program

# we can use float to convert text into number,
# but we can't use int to convert text into number,
# under some special case, like int(21.5) 
"""
print(float("80.95"))
print(int(float("890.756")))
"""
# some useful notes:
# print is clever, it can almost print anything
# like that:
print("just like 1+1 is ",1+1,"my heart for you is ",True)
# but for turtle, things are different
# you cannot do that:
# turtle.write("just like 1+1 is ",1+1,"my heart for you is ",True)
# but you can do that:
import turtle
turtle.write("just like 1+1 is "+str(1+1)+\
             "my heart for you is "+str(True))
