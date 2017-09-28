import sys
from printer import *
from complete import *
from add_remove import *

def intro():
    text = "\nCommand Line Todo Application\n"
    text += "=============================\n\n"
    text += "Command line arguments:\n"
    text += "-l   Lists all the tasks\n"
    text += "-a   Adds a new task\n"
    text += "-r   Removes an task\n"
    text += "-c   Completes an task\n\n"
    text += "Please choose a selector!"
    return text

def command_selector():
    if sys.argv[-1] == 'todo_list.py':
        print(intro())
    elif sys.argv[-1] == '-l':
        print_list()
    elif sys.argv[-1] == '-c':
        print("Please add your todos number after c!")
    elif sys.argv[-1] == '-u':
        print("Please add your todos number after u!")
    elif sys.argv[-1] == '-a':
        print("Please add your todo after a!")
    elif sys.argv[-1] == '-r':
        print("Please add your todos number after r!")
    elif sys.argv[-2] == '-c':
        make_complete(int(sys.argv[-1]))
    elif sys.argv[-2] == '-u':
        make_uncomplete(int(sys.argv[-1]))
    elif sys.argv[-2] == '-a':
        add_todo(sys.argv[-1])
    elif sys.argv[-2] == '-r':
        remove_todo(int(sys.argv[-1]))
    else:
        print("Undefined selector")