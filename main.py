import os
import yaml

todoFile = "data/todo.yaml"

def check_todo():
    with open(todoFile, 'r') as todo_file:
        todo = yaml.load(todo_file)

    for type_name in todo:
        # print(types)
        message = ""

        for task in todo[type_name]:
            message += "* "+task+"\n"
            #print (task)

        notify(title=type_name, message=message.strip())

def notify(message, title='my-reminder', icon='dialog-information'):
    os.system('notify-send "'+title+'" "'+message+'" --icon='+icon)


# def check_todo():
#     f = open("TODO.yaml")
#     for line in  f.readlines():
#         print(line.strip())


if __name__ =="__main__":
    check_todo()
    # notify(message='I am from my-reminder')
    # notify(message='I am from my-reminder \n Multiline Enabled')
    # notify(message='I am error message', icon='dialog-error')
