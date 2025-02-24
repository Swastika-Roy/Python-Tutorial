from operator import index
marks = [12,56,32,98,12,45,1,4]
# i = 0
# for mark in marks:
#     print(mark)
#     if(i == 3):
#         print("Awesome harry")
#     i += 1

# for index,mark in enumerate(marks):
#     print(mark)
#     if(index == 3):
#         print("Awesome")

for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index == 3):
        print("Awesome")
