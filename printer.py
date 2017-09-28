from open_and_save import *

def print_list():
    user_text = ""
    todo_list = create_dictonary()
    if todo_list == []:
        print("No todos for today! :)")
    else:
        i = 1
        for dict_item in todo_list:
            user_text += str(i) + " - "
            if dict_item["complete"]:
                user_text += "[x] "
            else:
                user_text += "[ ] "
            user_text += dict_item["todo"]
            i += 1
        print(user_text)