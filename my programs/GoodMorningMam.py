import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input('Enter hour : '))
# print(hour)

if(hour >= 0 and hour <12):
    print("Good Morning Mam")
elif(hour >= 12 and hour < 17):
    print("Good afternoon Mam")
elif(hour >= 17 and hour <20):
    print("Good Evening Mam")
else:
    print("Good night Mam")

