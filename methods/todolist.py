import threading

class Singleton_ToDoList:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.tasks = []
        return cls.__instance

    def get_tasks(self):
        with self.__lock:
            return self.tasks.copy()

    def get_task_by_index(self, index):
        with self.__lock:
            return self.tasks[index]

    def add_task(self, task):
        with self.__lock:
            self.tasks.append(task)

    def add_task_by_index(self, task, index):
        with self.__lock:
            self.tasks.insert(index, task)

    def add_multiple_tasks(self, tasks):
        with self.__lock:
            self.tasks.extend(tasks)

    def delete_task(self, task):
        with self.__lock:
            self.tasks.remove(task)
        
    def delete_task_by_index(self, index):
        with self.__lock:
            self.tasks.pop(index)

    def clear_tasks(self):
        with self.__lock:
            self.tasks.clear()