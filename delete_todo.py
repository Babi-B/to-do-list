from display import display
import create

deleted_items = []

def delete_todo():
    # Check if list is empty
    if len(create.todos) == 0:
        print("Your list is empty")
        print("")
        return

    display()
    print("Which do you wish to mark off")
    print("")
    try:
        num = int(input("Please, enter the item number ONLY: "))
    except ValueError:
        print("")
        print("Sorry, invalid input!")
        print("")
        print("Exiting program...")
        print("")
    
    # check if num false outside the range of list numbers
    if num > len(create.todos) and num < len(create.todos):
        print("")
        print("Sorry, invalid input!")
        print("")
        print("Exiting program...")
        print("")
        
        return
    item = create.todos[num - 1]
    deleted_items.append(item)
    create.todos.remove(item)
    print("")
    print(f"To-do updated successfully! '{item}' deleted")
    print("")
    print("Redirecting back to Main Menu")
    print("")

