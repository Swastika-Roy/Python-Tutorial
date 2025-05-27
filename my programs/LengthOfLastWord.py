s = s.strip()
length = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] != ' ':
        length += 1
    else:
        break
print(length)
