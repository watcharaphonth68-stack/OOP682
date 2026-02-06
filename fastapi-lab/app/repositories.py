from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate

class ITaskRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass
    
    @abstractmethod
    def update(self, task_id: int, task: Task) -> Optional[Task]:
        pass
    
class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(
            id=self.current_id,
            **task_in.dict()
        )
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update(self, task_id: int, task: Task) -> Optional[Task]:
        for i, existing_task in enumerate(self.tasks):
            if existing_task.id == task_id:
                self.tasks[i] = task
                return task
        return None
    
from sqlalchemy.orm import Session
from . import models_orm  # ต้องสร้าง SQLAlchemy Model แยก

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        return self.db.query(models_orm.Task).all()

    def create(self, task_in: TaskCreate) -> Task:
        db_task = models_orm.Task(**task_in.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def get_by_id(self, id: int):
        return self.db.query(models_orm.Task).filter(models_orm.Task.id == id).first()
    
    def update(self, task_id: int, task: Task) -> Optional[Task]:
        db_task = self.db.query(models_orm.Task).filter(models_orm.Task.id == task_id).first()
        if db_task:
            db_task.title = task.title
            db_task.description = task.description
            db_task.completed = task.completed
            self.db.commit()
            self.db.refresh(db_task)
            return db_task
        return None