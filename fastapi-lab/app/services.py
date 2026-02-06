from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Business logic could go here
        return self.repo.create(task_in)
    
    def mark_complete(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if task:
            task.completed = True
            return self.repo.update(task_id, task)
        return None