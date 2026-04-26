#True, False, and, not, or
"""
funny=True
friendly=False
alive=True
#not does the opposite
dead=not alive
#and--both inputs are True for the result to be True
ideal_partner=funny and friendly and alive
print(ideal_partner)
#or--just one is True, then the result is True
good_partner=(funny or friendly) and alive 
print(good_partner)
"""
"""
#some example
response=input('are you alive?(Yes/No)')
response=response=="Yes"
print(response)
"""
#tuple, list, text
mylist=[2,4,80,57,24,17,19,6]
mytuple=(2,4,80,57,24,17,19,6)
mytext="great"

#列表加列表
"""
mylist=mylist + [23,1]
print(mylist)
"""
# "+"只能把同种数据接在一起，例如list+list,不能是list+text
"""
mytext=mytext+mytext
print(mytext)
"""
#str--convert number into string(text)
"""
mytext=mytext+str(50)
print(mytext)
"""
#also, we can multiple the text/list/tuple

mytuple=mytuple*3
print(mytuple)


#提取列表中元素
"""
print(mylist[0])
print(mylist[-1])
print(mytext[-2])
"""
#slicing
"""
print(mylist[2:5])
mylist[2:5]=[1,3,607]
print(mylist)
"""
#2D list
#you can put anything in the list,even a list
thing=[[20,21,22,23,28],
       [20,47,90,10,89],
       [11,17,64,27,81]]
print(thing[2][2])
# the output is '64'
print(len(thing))
# the output is '3'




