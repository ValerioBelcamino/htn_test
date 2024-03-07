#!/usr/bin/env python
import sys
import gtpyhop
from methods.todolist import Singleton_ToDoList
domain = gtpyhop.Domain('test')
from methods.methods import *
from actions.actions import *
from state.state import state
from change_plan import change_plan_loop
from threading import Thread

sys.setrecursionlimit(3000)


def main():
    gtpyhop.current_domain = domain

    state.display('This is initial state')

    # state1 = state.copy()

    gtpyhop.verbose = 3

    gtpyhop.print_domain()

    # todo_list = Singleton_ToDoList()
    # todo_list.add_multiple_tasks([('method1',),
    #                               ('method2',),
    #                               ('method3',),
    #                               ('method4',)])

    todo_list = [('method1',),
                ('method2',),
                ('method3',),
                ('method4',)]

    print(todo_list)

    c_p_loop_th = Thread(target=change_plan_loop, args=(todo_list,)).start()
    result = gtpyhop.find_plan(state, todo_list)
    print(todo_list)
    return


if __name__ == "__main__":
    main()
