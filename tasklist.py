#have a help command
#have a show command
#clean code up in general

#make a list to hold our items
todo_list = []
def show_help():
#print instructiosn
    print("What should we do today?")
    print("""
Enter 'Done' to stop adding items
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
    print("Here's your list:")

    for item in todo_list:
        print (item)

def add_to_list(new_task):
        todo_list.append(new_task)
        print("Added {}. List now has {} items.".format(new_task, len(todo_list)))

show_help()

while True:
    #ask for new items
    new_task = input("> ")

    if new_task =="DONE":
        break
    elif new_task =="HELP":
        show_help()
        continue
    elif new_task =="SHOW":
        show_list()
        continue
    add_to_list(new_task)

show_list()

#be able to quit the app
