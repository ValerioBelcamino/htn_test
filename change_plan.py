#!/usr/bin/env python
from methods.todolist import Singleton_ToDoList

def change_plan_loop(todo_list):
    while True:
        print('Current plan:')
        print(todo_list)

        user_input = input("Enter 'a' to add or 'd' to delete: ")
        if user_input == 'a':
            print('choose a task to add to the plan')
            user_input_arg = input("Task: ")
            # add code here to add to the plan
            todo_list.append((user_input_arg,))
            pass
        elif user_input == 'd':
            print('choose a task to delete from the plan')
            user_input_arg = input("Task: ")
            # todo_list.delete_task_by_index(int(user_input_arg))
            todo_list.pop(int(user_input_arg))
            # add code here to delete from the plan
            pass
        elif user_input == 'q':
            print('Return')
            return
            # add code here to delete from the plan
            pass
        else:
            print("Invalid input. Please enter 'a' to add or 'd' to delete.")
