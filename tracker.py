from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, item_id, title):
        self._item_id = item_id
        self._title = title
        self._is_completed = False

    def get_item_id(self):
        return self._item_id

    def get_is_completed(self):
        return self._is_completed

    def set_completed(self):
        self._is_completed = True

    def get_status_string(self):
        if self._is_completed == True:
            return "Completed"
        else:
            return "Pending"

    @abstractmethod
    def get_details(self):
        pass

class WorkTask(Item):
    def __init__(self, item_id, title, project):
        super().__init__(item_id, title)
        self._project = project

    def get_details(self):
        status = self.get_status_string()
        info = "[Work - Project: " + self._project + "] ID: " + str(self.get_item_id()) + " | Title: " + self._title + " | Status: " + status
        return info

class PersonalTask(Item):
    def __init__(self, item_id, title, priority):
        super().__init__(item_id, title)
        self._priority = priority

    def get_details(self):
        status = self.get_status_string()
        info = "[Personal - Priority: " + self._priority + "] ID: " + str(self.get_item_id()) + " | Title: " + self._title + " | Status: " + status
        return info

class TaskTracker:
    def __init__(self):
        self._tasks_list = []

    def add_task(self, task):
        self._tasks_list.append(task)

    def complete_task(self, task_id):
        for task in self._tasks_list:
            if task.get_item_id() == task_id:
                task.set_completed()
                return True
        return False

    def delete_task(self, task_id):
        for task in self._tasks_list:
            if task.get_item_id() == task_id:
                self._tasks_list.remove(task)
                return True
        return False

    def show_tasks(self):
        if not self._tasks_list:
            print("No tasks found.")
            return 
        print("\n--- Current Tasks ---")
        for task in self._tasks_list:
            print(task.get_details())

tracker = TaskTracker()
task1 = WorkTask(101, "Fix codebase bugs", "Alpha App")
task2 = PersonalTask(102, "Buy groceries", "High")

tracker.add_task(task1)
tracker.add_task(task2)
tracker.show_tasks()

tracker.complete_task(101)
tracker.show_tasks()

tracker.delete_task(102)
tracker.show_tasks()
