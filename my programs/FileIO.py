#Reading a file in python

# f = open('myfile.txt','r') #to read file we use 'r'
# f = open('myfile.txt','rt') #to read text related files we use 'rt'
# f = open('myfile.txt','rb') #to read file as binary type we use 'rb'
# text = f.read()
# print(text)
# f.close()


#appending text inside a file in python

f = open('myfile.txt','a')
f.write(" I study in Haldia institute of Technology.")
f.close()



#If we use with keyword here, then we do not require to close any file

with open("myfile2.txt",'a') as f:
    f.write(" How are you ?")



#Writing a file in python

# f = open('myfile2.txt','w')
# f.write("Hello, How are you?")
# f.close()



