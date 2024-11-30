from Model.base_model import BaseScreenModel
from Model.database import Task


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()

        self.tasks: list[Task] = []

    def get_tasks_list(self, owner_id: int) -> list[Task] | None:
        tasks = self._db.get_data_by_model(model=Task(user_id=owner_id), fetch_all=True)

        if tasks is not None:
            self.tasks = tasks
        
        self.notify_observers('main screen')
