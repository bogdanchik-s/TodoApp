from kivy.graphics.svg import Svg
from kivymd.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)

from View.base_screen import BaseScreenView


class LoginScreenView(BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.dialog: MDDialog = None

    def show_dialog(self, title:str, text: str):
        self.dialog = MDDialog(
            MDDialogHeadlineText(
                text=title,
            ),
            MDDialogSupportingText(
                text=text
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text='Ок'),
                    style="text",
                    on_release=self.close_dialog
                ),
                spacing="8dp"
            ),
        )
        self.dialog.open()

    def close_dialog(self, btn):
        if self.dialog is not None:
            self.dialog.dismiss()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        if self.model.user.id is not None:
            self.app.current_user = self.model.user
            self.app.manager_screens.current = 'main screen'
        else:
            self.show_dialog(title='Ошибка', text='Неверный логин или пароль')
