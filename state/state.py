from gtpyhop import State
from threading import Lock

state = State("state_test")
state.state_variable = None

# class Singleton_State:

#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton_State, cls).__new__(cls)
#         return cls.instance

#     def __init__(self):
#         self.state = State("state_test")
#         self.state.state_variable = None
#         self.state_lock = Lock()

#     def get_state(self):
#         self.state_lock.acquire()
#         state_copy = self.state.deepcopy()
#         self.state_lock.release()
#         return state_copy

#     def set_state(self, new_state):
#         self.state_lock.acquire()
#         self.state = new_state.deepcopy()
#         self.state_lock.release()

