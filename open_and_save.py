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
        return todo_list
        fr.close()
    except IOError:
        print("Unable to read file: todo_list.txt")

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