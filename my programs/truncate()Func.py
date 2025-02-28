with open('sample.txt','w') as f:
    f.write('Proud of India')
    f.truncate(5)

with open('Sample.txt','r') as f:
    print(f.read())