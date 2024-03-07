import gtpyhop
import time
from methods.todolist import Singleton_ToDoList

def method1(state):
    print('method1')
    time.sleep(5)
    return [('action1',),
            ('action2',)]

def method2(state):
    print('method2')
    time.sleep(5)
    return [('action3',),
            ('action4',)]

def method3(state):
    print('method3')
    time.sleep(5)
    return [('action5',),
            ('action6',),
            ('action7',)]

def method4(state):
    print('method4')
    time.sleep(5)
    return [('action8',),
            ('action9',),
            ('action10',)]

def global_method(state, task_list):
    print('global_method')
    return task_list

gtpyhop.declare_task_methods('method1', method1)
gtpyhop.declare_task_methods('method2', method2)
gtpyhop.declare_task_methods('method3', method3)
gtpyhop.declare_task_methods('method4', method4)
gtpyhop.declare_task_methods('global_method', global_method)