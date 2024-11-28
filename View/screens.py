# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController

screens = {
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
    },
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
}