class Item:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.is_completed = False

    def get_details(self):
        if self.is_completed == True:
            status = "Completed"
        else:
            status = "Pending"
        
        info = "ID: " + str(self.item_id) + " | Title: " + self.title + " | Status: " + status
        return info


class WorkTask(Item):
    def __init__(self, item_id, title, project):
        super().__init__(item_id, title)
        self.project = project

    def get_details(self):
        if self.is_completed == True:
            status = "Completed"
        else:
            status = "Pending"
        
        info = "[Work - Project: " + self.project + "] ID: " + str(self.item_id) + " | Title: " + self.title + " | Status: " + status
        return info


class PersonalTask(Item):
    def __init__(self, item_id, title, priority):
        super().__init__(item_id, title)
        self.priority = priority

    def get_details(self):
        if self.is_completed == True:
            status = "Completed"
        else:
            status = "Pending"
            
        info = "[Personal - Priority: " + self.priority + "] ID: " + str(self.item_id) + " | Title: " + self.title + " | Status: " + status
        return info


class TaskTracker:
    def __init__(self):
        self.tasks_list = []

    def add_task(self, task):
        self.tasks_list.append(task)

    def complete_task(self, task_id):
        for task in self.tasks_list:
            if task.item_id == task_id:
                task.is_completed = True
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks_list:
            if task.item_id == task_id:
                self.tasks_list.remove(task)
                return True
        return False

    def show_tasks(self):
        if not self.tasks_list:
            print("No tasks found.")
            return
        
        print("\n--- Current Tasks ---")
        for task in self.tasks_list:
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
