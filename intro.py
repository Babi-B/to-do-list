from time import sleep
from create import create

print("******************************************************")
print("")
print("               WELCOME ")
sleep(.2)
print("")
print("What do you wish to do? (Please enter a number)")
print("")
print("1. Add a to-do")
print("2. View all your to-do's")
print("3. Mark off a to-do")
print("")
sleep(.2)
print("")

num = input("Please enter the corresponding number: ")
while not num.isnumeric():
    print("")
    num = input("PLEASE ENTER A NUMBER: ")

userInput = int(num)

match userInput:
    case 1:
        create()
    case 2:
        create()
    case 3:
        create()
    case _:
        print("")
        print("Invalid input!")
        sleep(.2)
        print("")
        print("")
        print("            Program shutting down...")
        print("")
        print("")
        sleep(2)


    





