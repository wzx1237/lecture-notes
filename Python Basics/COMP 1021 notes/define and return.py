
# daily task--text slicing
x="cats eat bats for hats"
print(x[::6])
# the outcome is 'cash'
x='potatoes are yummy'
print(x[4:6]+x[15]+x[3:8])
# the outcome is 'tomatoes'

#def and return
def get_info(current_year,birth_year):
    age = current_year-birth_year
    return age
"""
year=int(input('current year'))
years=int(input('your birth year'))
result=get_info(year,years)
print(result)
"""

#convert number
"""
def convert_number_into(number):
    list=[]
    y=[]
    count_0=0
    digital=1
    while True and number>=1 :
        b=2**digital
        if int(number/b)>1  :
            digital=digital+1
        elif int(number/b)<=1 :
            list.append(digital)
            number=number-b
            digital=1
    print(list)
    for i in range(list[0]+1):
        y.append(0)
    for i in range(len(list)):
        y[-list[i]-1]=1
    result=""
    for i in range(len(y)) :
        result=result+str(y[i])
    return result
numbers=int(input("what's number you want to convert?"))
result=convert_number_into(numbers)
print(result)
"""
# 一个函数，一旦它被return了，
# 函数中在return后面的部分不会再运行
def absolute(x):
    if x<0:
        return -x
    return x
print(absolute(-4))
# output
# 4
def wrong_absolute(x):
    return x
    if x<0:
        return -x
print(wrong_absolute(-4))
# output:
# -4
# 这里你可以看到：在return后，'if x<0:'并没有被执行
