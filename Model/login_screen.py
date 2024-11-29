from Model.base_model import BaseScreenModel
from .database import User

class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()

        self.user = User()
        self._user_password = None

    def get_user_data(self):
        if self.user.username is not None and self._user_password is not None:
            user = self._db.get_data_by_model(model=self.user, extra_fields={'password': self._user_password})

            if user is not None:
                self.user = user

        self.notify_observers('login screen')
    
    def set_user_data(self, key, value):
        if key != 'password':
            setattr(self.user, key, value)
        else:
            self._user_password = value
