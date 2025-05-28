def  Palindrome(s):
    s = s.replace(" ","").lower()
    return s==s[::-1]

print(Palindrome("madam"))