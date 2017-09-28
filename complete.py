from open_and_save import *

def make_complete(number):
    todo_list = create_dictonary()
    if number <= len(todo_list) and number > 0:
        todo_list[number-1]["complete"] = True
    else:
        print("The number is out of range!")
    save_to_file(todo_list)

def make_uncomplete(number):
    todo_list = create_dictonary()
    if number <= len(todo_list) and number > 0:
        todo_list[number-1]["complete"] = False
    else:
        print("The number is out of range!")
    save_to_file(todo_list)