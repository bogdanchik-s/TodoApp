from Model.base_model import BaseScreenModel
from .database import Task


class TaskScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.task_screen.TaskScreen.TaskScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()

        self.task = Task()
    
    def set_task_data(self, key, value):
        setattr(self.task, key, value)

    def save_task(self):
        self._db.insert_data_by_model(model=self.task)
