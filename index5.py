# Assignment 5
# Name: Nelab Khalily
# Description: nelabkhalily@gmail.com

import random

# it checks what users enters is single and a digit
# returns bool values
def isSingleDigit(userStr):
    if userStr.isdigit() and len(userStr) == 1:
        return True
    else:
        return False

# based on the parameter it loops through the function and adds randomly selected integers to the list
# returns the random digit list
def createCodeList(num):
    varList = []
    for num in range(num):
        randomDigit = random.randrange(10)
        varList.append(randomDigit)
    return varList
def displayHints(codeList, userList, num):
    print("\nGenerating hints...")
    hintsNum = 0


        randomDigit = random.randrange(10)
        varList.append(randomDigit)
    for index in range(num):
        digit = userList[index]
        if digit == codeList[index]:
            print("index", index, "->", digit, "is correct")
            hintsNum = hintsNum + 1
        count = codeList.count(digit)

# it checks the user list eith the random list to see if a number at an index matches or not
def displayHints(codeList, userList, num):
    print("\nGenerating hints...")
    hintsNum = 0

    for index in range(num):
        digit = userList[index]
        if digit == codeList[index]:
            print("index", index, "->", digit, "is correct")
            hintsNum = hintsNum + 1
        count = codeList.count(digit)


        print()

# in main function we complete the code by calling the functions we have made
def main():
    digitsNum = 3
    code = createCodeList(digitsNum)
    guess = createUserList(digitsNum)
    guessNum = 1

    while guess != code:
        displayHints(code, guess, digitsNum)
        guess = createUserList(digitsNum)
        guessNum = guessNum + 1
    print("\n You Cracked the Code! in", guessNum, "guesses!")

main()
