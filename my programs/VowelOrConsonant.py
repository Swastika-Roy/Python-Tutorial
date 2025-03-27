def IsVowel(ch):
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A"
            or ch == "E" or ch == "I" or ch == "O" or ch == "u"):

        print("VOWEL")
    else:
        print("CONSONANT")

ch = input("Enter character : ")
IsVowel(ch)