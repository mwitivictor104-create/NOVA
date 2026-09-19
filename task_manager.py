class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        item = {
            "id": len(self.tasks) + 1,
            "task": task,
            "completed": False
        }

        self.tasks.append(item)
        return item

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task

        return None

    def list_tasks(self):
        return self.tasks


manager = TaskManager()
