from timeit import repeat
import MathFunctions as mfc
import os


stop = True
operation = 0
first = 0
second = 0

os.system('cls')
while stop:
    print("Input two numbers")
    first = float(input())
    second = float(input())

    print("Choose an Operation")
    print("Sum: 1")
    print("Minus: 2")
    print("Plus: 3")
    print("Division: 4")
    operation = input()
    if(operation is "1"):
        result = mfc.sum(first,second)
        print(result)
    elif(operation is "2"):
        result = mfc.minus(first,second)
        print(result)
    elif(operation is "3"):
        result = mfc.plus(first,second)
        print(result)   
    elif(operation is "4"):
        result = mfc.division(first,second)
        print(result)     
    else:
        print("Choose a valid operation")

    print("Do you want to operate again?")
    stop2 = True
    while stop2:
        print("1 - Yes")
        print("2 - No")
        repeat = input()
        if(repeat is "1"):
            stop2 = False
            stop = True
        elif(repeat is "2"):
            stop2 = False
            stop = False
        else:
            print("put a valid number")
    os.system('cls')

