from time import sleep
from exceptions import InvalidInput
from intro import intro

todos = []



def create():
    add_more = True

    print("")
    print("               Okay! Let's write ")
    print("")
    todos.append(input("Add your todo: "))

    while add_more:
        print("")
        print("Do you wish to add more?")
        print("")

        try:
            userInput = input("Type 1 for 'yes' and 0 for 'no': ")
            add_more = True if (int(userInput) == 1) else False
        except ValueError:
           print("")
           return print("Invalid Input. Next time, please enter either 0 or 1")
        
        # Custom exception
        # if userInput != "1" or userInput != "0":
        #    raise InvalidInput(userInput)
        else:
            if int(userInput) == 0:
                print("")
                print("Loading main menu....")
                print("")
                add_more = False
            else:
                print("")
                todos.append(input("Add your todo: "))
                print("")
                print("    To-do added!")
    return todos

