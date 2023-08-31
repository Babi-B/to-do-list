from time import sleep
from intro import intro
from create import create
from display import display
from delete_todo import delete_todo

def app():
    runApp = True

    while runApp:
            # run the intro screen
        num = intro()

        # Check if num is a numeric
        while not num.isnumeric():
            print("")
            num = input("PLEASE ENTER A NUMBER: ")

        # Convert num to an integer
        userInput = int(num)

        match userInput:
            case 1:
                create()
                sleep(1)
            case 2:
                display()
                print("Back to the main menu")
                sleep(1)
            case 3:
                delete_todo()
                sleep(1)
            case 4:
                create()
            case 5:
                print("")
                print("Thank you for using this app!")
                print("")
                sleep(1)
                runApp = False
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
app()