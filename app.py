import csv

todos = []
stop = False

def get_todos():
    #add_one_task()
    global todos
    return todos

def add_one_task(title):
    return get_todos().append(title)

def print_list():
    global todos
    y=1
    print("Lista de tareas:")
    for x in todos:
        print(str(y) + ";" + x)
        y=y+1


def delete_task(number_to_delete):
    # your code here
    number_to_delete=int(number_to_delete)-1
    return get_todos().pop(number_to_delete)
    

def save_todos():
    # your code here
    global todos
    todos_file=""
    i=0
    for tareas in todos:
       # todos_file = todos_file + ";" + tareas
        
        if i == 0:
            todos_file = todos_file + tareas
            i=i+1
        else:
            todos_file = todos_file + "," + tareas
        
    file_to_save = open("todos.csv","w+")
    file_to_save.write(todos_file)
    file_to_save.close()

def load_todos():
    # your code here
    global todos
    file=open("todos.csv","r")
    csv_f = csv.reader(file)
    i=1
    first=True
    for row in csv_f:
#        print(row)
        for x in row:
            todos.append(x)
    print(todos)
    file.close()
    #print(todos)
    #return todos

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")