todo_list = []

while True:
    print('\nOptions:')
    print('1. Add task')
    print('2. View tasks')
    print('3. Mark task as completed')
    print('4. Remove completed tasks')
    print('5. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        task = input('Enter a new task: ')
        todo_list.append({'task': task, 'completed': False})
        print("Task added!")

    elif choice == '2':
        if not todo_list:
            print("No tasks added yet.")
        else:
            for i, task in enumerate(todo_list):
                status = 'Done' if task['completed'] else 'Not Done'
                print(f'{i + 1}. {task["task"]} - {status}')

    elif choice == '3':
        if not todo_list:
            print("No tasks to mark.")
        else:
            task_number = int(input('Enter task number to mark as completed: ')) - 1
            if 0 <= task_number < len(todo_list):
                todo_list[task_number]['completed'] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == '4':
        todo_list = [task for task in todo_list if not task['completed']]
        print("Completed tasks removed!")

    elif choice == '5':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid option! Please choose again.")
