
from View.MainScreen.main_screen import MainScreenView


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_view(self) -> MainScreenView:
        return self.view

    def load_tasks(self):
        if self.view.app.current_user is not None:
            self.model.get_tasks_list(
                owner_id=self.view.app.current_user.id
            )
    
    def create_task(self):
        self.view.app.manager_screens.current = 'task screen'

    def edit_task(self):
        pass

    def delete_task(self):
        pass
