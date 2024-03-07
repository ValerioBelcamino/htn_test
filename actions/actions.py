import gtpyhop
import time 
import random
import rospy
from state.rigid import rigid
import copy


def action1(state):
    print('     action1')
    time.sleep(1.0)
    state.state_variable = 'action1'
    return state

def action2(state):
    print('     action2')
    time.sleep(1.0)
    state.state_variable = 'action2'
    return state

def action3(state):
    print('     action3')
    time.sleep(1.0)
    state.state_variable = 'action3'
    return state

def action4(state):
    print('     action4')
    time.sleep(1.0)
    state.state_variable = 'action4'
    return state

def action5(state):
    print('     action5')
    time.sleep(1.0)
    state.state_variable = 'action5'
    return state

def action6(state):
    print('     action6')
    time.sleep(1.0)
    state.state_variable = 'action6'
    return state

def action7(state):
    print('     action7')
    time.sleep(1.0)
    state.state_variable = 'action7'
    return state

def action8(state):
    print('     action8')
    time.sleep(1.0)
    state.state_variable = 'action8'
    return state

def action9(state):
    print('     action9')
    time.sleep(1.0)
    state.state_variable = 'action9'
    return state

def action10(state):
    print('     action10')
    time.sleep(1.0)
    state.state_variable = 'action10'
    return state

gtpyhop.declare_actions(action1, 
                        action2, 
                        action3, 
                        action4, 
                        action5,
                        action6, 
                        action7,
                        action8, 
                        action9, 
                        action10)