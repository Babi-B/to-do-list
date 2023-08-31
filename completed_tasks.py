import delete_todo

def completed():
    counter = 1

    if len(delete_todo.deleted_items) == 0:
        print("")
        print("You haven't marked off any to-do's yet")
    else:
        print("")
        print("Here are your completed to-do's")
        print("")
        for deleted_item in delete_todo.deleted_items:
            print(f"{counter}. {deleted_item}")
            print("")
            counter += 1
    print("")