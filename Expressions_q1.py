def LetterMake(letter):
    letterOrd = ord(letter) # get first code point

    beforeLetter = chr(letterOrd - 1) # get letter before and after
    afterLetter = chr(letterOrd + 1) # get letter after

    beforeOrd = ord(beforeLetter)
    afterOrd = ord(afterLetter)

    print(letter + "'s code point is " + str(letterOrd)) # print the letter and its code point
    print("before " + letter + " is " + beforeLetter + ", code point " + str(beforeOrd)) # print letter before
    print("after " + letter + " is " + afterLetter + ", code point " + str(afterOrd)) # print letter after

userLetter = input("Enter a single capital letter: ") # take input

if len(userLetter) == 1: # makes sure there is only one letter
    LetterMake(userLetter) # function with UserLetter in mind
else:
    print("Please enter a single letter")
