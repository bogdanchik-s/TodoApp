
from View.TaskScreen.task_screen import TaskScreenView


class TaskScreenController:
    """
    The `TaskScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.task_screen.TaskScreenModel
        self.view = TaskScreenView(controller=self, model=self.model)

    def get_view(self) -> TaskScreenView:
        return self.view

    def back_button_click(self):
        self.view.app.manager_screens.current = 'main screen'

    def set_task_data(self, key, value):
        self.model.set_task_data(key, value)
        self.model.set_task_data('user_id', self.view.app.current_user.id)
    
    def submit_button_click(self):
        self.model.save_task()
        self.back_button_click()
