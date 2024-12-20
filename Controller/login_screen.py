from View.LoginScreen.login_screen import LoginScreenView


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = LoginScreenView(controller=self, model=self.model)

    def get_view(self) -> LoginScreenView:
        return self.view

    def set_user_data(self, key, value):
        self.model.set_user_data(key, value)

    def login_button_click(self):
        self.model.get_user_data()
