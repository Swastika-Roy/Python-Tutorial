f = open('myfile4.txt','w')
lines = ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()