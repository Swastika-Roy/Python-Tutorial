# countries = ("Spain","England","Russia","India")
# print(countries)
#
# temp = list(countries) #coverting tuple into list
#
# temp.pop(2) #remove item
# print(temp)
#
# temp.append("Japan") #add item
# print(temp)
#
# temp[0] = "America" #cnange item
# print(temp)
#
# countries = tuple(temp)  #converting list into tuple
#
# print(countries)

#Merge two tuples
# Fruits = ("Apple","Mango","Banana","Guava")
# Vegetables = ("Cucumber","Potato","Brinjal","Spinach")
# Veg = Fruits+Vegetables
# print(Veg)

#InbuiltMethodsinTuple
tp = (3,5,6,8,1,2)
ans = tp.index(5,1,8)
print(ans)
# res = tp.count(1)
# print(res)
# print(tp.count(2))
# print(tp.index(2))
print(len(tp))