# 11.20 dictionary
mydic={"cat":"animal goes miaowww","dog":"animal goes wanggg"}
print(mydic["cat"])# here we must use:""
print(mydic["dog"])
# output:
# "animal goes miaowww"
# "animal goes wanggg"



# add element
mydic["ant"]="insect, very small"
print(mydic)
# output:
# "cat":"animal goes miaowww","dog":"animal goes wanggg", "ant":"insect, very small"
# is mapped to...

rooms={3554:"rossiter",3553:"gibson"}
print(rooms[3554])
# output:"rossiter"




# change the element
rooms[3553]="desmond"
print(rooms[3553])
# output:"desmond"



#delete element
# use'del'
# you can del everything--turtle,list,tuple,variable...
del rooms[3553]
print(rooms)
# output:
# 3554:"rossiter"



positions={"HK":[22.303,114.177]}
positions["macao"]=[22.303,115.177]
print(positions["HK"][0])
# output:22.303





# if you wanna go through everything in the dictionary
# use ".items"
for key,value in mydic.items():
    # here we must use: "mydic.items"
    # once we use: "mydic", python will crash
    print(key,value)
# output:
#cat animal goes miaowww
#dog animal goes wanggg
#ant insect, very small

for k, v in mydic.items():
    print(k)
#cat
#dog
#ant

# if you want to go through values in the dictionary
# you can use ".values"
for x in mydic.values():
    print(x)
#animal goes miaowww
#animal goes wanggg
#insect, very small

# also, if you want to go through keys in the dictionary
# you can use ".keys"
for x in mydic.keys():
    print(x)
# cat
# dog
# ant

# 如果你什么都不加，
# python会默认你要print的是key
for x in mydic:
    print(x)
# output:
# cat
# dog
# ant





# another example:
pokemon_list = {
 "Aerodactyl" :
 {"Category" : "Very Rare",
 "Level" : 8, "Position" : (100, 45)},
 "Arbok" :
 {"Category" : "Rare",
 "Level" : 1, "Position" : (-4, 105)},
 "Pikachu" :
 {"Category" : "Rare",
 "Level" : 8, "Position" : (230, 130)},
}
# 在这个dictionary里
# 将pokemon的名字作为了key
for pokemon in pokemon_list:
    level=pokemon_list[pokemon]["Level"]
    print(pokemon)
    print(level)
# output:
"""
Aerodactyl
8
Arbok
1
Pikachu
8
"""

# tips: you can't use a list as you key,
# because list can be changed,
# which might confuse you
# so you can use a tuple instead


# some example:
language_skills={'Native': ['chinese'],\
                 'fluent': ['english'],\
                 'elementary':['japanese']}
del language_skills['elementary']
print(language_skills)
# the output is:
"""
{'Native': ['chinese'], 'fluent': ['english']}
"""

###################
###################
# state diagrams

