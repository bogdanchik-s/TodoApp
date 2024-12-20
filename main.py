"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""

from kivy.config import Config

Config.set('graphics', 'width', 428)
Config.set('graphics', 'height', 626)
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'maxfps', 120)

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from View.screens import screens
from Model.database import User


class TodoApp(MDApp):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()
        self.current_user: User = None

    def build(self) -> MDScreenManager:
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Green'
        
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)
        
        self.manager_screens.current = 'login screen'


TodoApp().run()
