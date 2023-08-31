import create

def display():
    counter = 1

    if len(create.todos) == 0:
        print("Your list is empty")
    else:
        print("")
        print("Here are your to-do's")
        print("")
        for todo in create.todos:
            print(f"{counter}. {todo}")
            print("")
            counter += 1
    print("")
