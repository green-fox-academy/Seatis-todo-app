from open_and_save import *

def add_todo(todo_text):
    todo_list = create_dictonary()
    if todo_list != []:
        todo_list[-1]["todo"] = todo_list[-1]["todo"][0:] + "\n"
    todo_dict = {}
    todo_dict["complete"] = False
    todo_dict["todo"] = todo_text
    todo_list.append(todo_dict)
    save_to_file(todo_list)

def remove_todo(number):
    todo_list = create_dictonary()
    if number <= len(todo_list) and number > 0:
        del todo_list[number-1]
    else:
        print("The number is out of range!")
    save_to_file(todo_list)