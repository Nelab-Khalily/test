# Assignment 5
# Name: Nelab Khalily
# Description: nelabkhalily@gmail.com

import random

# it checks what users enters is single and a digit
# returns bool values
def isSingleDigit(userStr):
    if userStr.isdigit() and len(userStr) == 1:
        return True

# based on the parameter it loops through the function and adds randomly selected integers to the list
# returns the random digit list
def createCodeList(num):
    varList = []
    for num in range(num):
        randomDigit = random.randrange(10)
        varList.append(randomDigit)
    return varList

# it creates a list through which user enters values on indexes based on the given num to loop
# returns the list user entered value for
def createUserList(num):
    print("The number of digits in the code is ", num)
    varList = []
    for num in range(num):
        userStr = input("Enter a digit at index " + str(num) + ": ")
        while not isSingleDigit(userStr):
            userStr = input("Enter a digit at index " + str(num) + ": ")
        userDigit = int(userStr)
        varList.append(userDigit)
    print("Your guess is", varList)
    return varList

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

        if count > 0:
            print("index", index, "->", digit, "occurs", count, "time(s)")
            hintsNum = hintsNum + 1

        if hintsNum => 0:
            print("No correct digits")

        print()

# in main function we complete the code by calling the functions we have made
def main():
    code = createCodeList(digitsNum)
    guess = createUserList(digitsNum)
    guessNum = 1

    while guess != code:
        displayHints(code, guess, digitsNum)
        guess = createUserList(digitsNum)
        guessNum = guessNum + 1
    print("\n You Cracked the Code! in", guessNum, "guesses!")

main()