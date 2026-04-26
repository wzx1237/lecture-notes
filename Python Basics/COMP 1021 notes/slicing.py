#10月16日笔记
#slicing

x=[4,8,80,78,47,28,'good',7956]

#using negative number in list
#-1 means the last one
"""
print(x[-1])
"""
# the output is 7956

#from list[3] to list[5], do not include the target number
#list[start_number : finish_number : step]
print(x[3:6:2])
# the output is [78,28]
print(x[7:2:-2])
# the output is [7956,28,78]

#留空格也能跑
print(x[ :2])
# the output is [4,8]
print(x[1: ])
# the output is [8,80,78,47,28,'good',7956]
#very similar to range

#矩阵
"""
things=[[28,78,68,67,4],
        [90,10,9 ,89,5],
        [43,6 ,1 ,3 ,2]]
print(things[1][2])
"""
print(x[::-1])#==reverse the list
#对音频来讲，list[::2]可以加快频率

# some special case:
x=[1,2,3,4,5]
print(x[4:-1:-1])
# output:
# []
print(x[0:5])
# output:
# [1, 2, 3, 4, 5]

# also, we can use slicing to reverse the list
print(x[::-1])
# output:
# [5, 4, 3, 2, 1]



# Rounding:
# if you want python to round a float
# to the closest integer
# one way if to use round()
# however, if the float is in the middle of
# 2 integers, like 1.5
# python will round to the nearest even number

for num in (1.3,7.89,67.5,68.5,10.0):
    print(round(num),end=" ")
# the output:
# 1 8 68 68 10
