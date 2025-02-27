# f = open('myfile3.txt','r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"marks of student {i} in Maths : {m1*2}")
#     print(f"marks of student {i} in computer : {m2*2}")
#     print(f"marks of student {i} in science : {m3*2}")
# f.close()

f = open("myfile.txt",'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)