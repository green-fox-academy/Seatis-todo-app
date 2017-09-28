import sys


def add_todo(todo_text):
    todo_list = create_dictonary()
    todo_list[-1]["todo"] = todo_list[-1]["todo"][0:] + "\n"
    todo_dict = {}
    todo_dict["complete"] = False
    todo_dict["todo"] = todo_text
    todo_list.append(todo_dict)
    save_to_file(todo_list)

def save_to_file(todo_list_updated):
    try:
        server_text = ""
        for dict_item in todo_list_updated:
            if dict_item["complete"]:
                server_text += "1 "
            else:
                server_text += "0 "
            server_text += dict_item["todo"]
        fw = open("todo_list.txt", "w")
        fw.write(server_text)
        fw.close()
    except IOError:
        print("Unable to write file: files/decrypt-lines.txt")


def command_selector():
    if sys.argv[-1] == '-l':
        print_list()
    elif sys.argv[-2] == '-c':
        num = int(sys.argv[-1])
        make_complete(num)
    elif sys.argv[-2] == '-u':
        num = int(sys.argv[-1])
        make_uncomplete(num)
    elif sys.argv[-2] == '-a':
        add_todo(sys.argv[-1])
    else:
        print("Please choose a selector!")

def make_complete(number):
    todo_list = create_dictonary() 
    todo_list[number-1]["complete"] = True
    save_to_file(todo_list)

def make_uncomplete(number):
    todo_list = create_dictonary() 
    todo_list[number-1]["complete"] = False
    save_to_file(todo_list)

def create_dictonary():
    try:  
        todo_list = []
        fr = open('todo_list.txt', "r")
        lines_list = fr.readlines()
        for line in lines_list:
            todo_dict = {}
            if line[0] == "0":
                todo_dict["complete"] = False
            else:
                todo_dict["complete"] = True
            todo_dict["todo"] = line[2:]
            todo_list.append(todo_dict)
        # todo_list[-1]["todo"] = todo_list[-1]["todo"][0:] + "\n"
        return todo_list
        fr.close()
    except IOError:
        print("Unable to read file: todo_list.txt")


def print_list():
    user_text = ""
    todo_list = create_dictonary()
    for dict_item in todo_list:
        if dict_item["complete"]:
            user_text += "[x] "
        else:
            user_text += "[ ] "
        user_text += dict_item["todo"]
    print(user_text)
    # print (todo_list)
    
        




def main():
    command_selector()

main()

# print(sys.argv)