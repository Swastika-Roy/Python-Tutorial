# l = [2,3,4]
# print(l)
# print(type(l))
#
# l1 = ["Ram","Mohan","Sohan"]
# print(l1)
# print(type(l1))
# print(l1[0])
# print(l1[1])
# print(l1[2])

# l2 = ["Sita","Gita",1,2,True]
# print(l2)
# print(type(l2))
# print(l2[-3]) # l2[len(l2) - 3]
# print(l2[1:-1:2])

# if "1" in l2:
#     print("Yes")
# else:
#     print("No")
#
# if "arr" in "Harry":
#     print("yes")
# else:
#     print("No")


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
