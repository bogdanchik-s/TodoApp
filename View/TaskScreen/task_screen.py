from kivymd.uix.pickers import MDDockedDatePicker
from kivy.metrics import dp

from View.base_screen import BaseScreenView


class TaskScreenView(BaseScreenView):
    def on_pre_enter(self):
        self.ids.task_title.text = ''
        self.ids.task_description.text = ''
        self.ids.task_expire_date.text = ''

    def on_text_callback(self, task_property_name: str, task_property_value: str):
        if 0 < len(self.ids.task_title.text) <= 50 and 0 < len(self.ids.task_description.text) <= 255 and self.ids.task_expire_date.text != '':
            self.ids.submit_button.disabled = False
        else:
            self.ids.submit_button.disabled = True
        
        self.controller.set_task_data(key=task_property_name, value=task_property_value)

    def show_date_picker(self, focus):
        def on_ok_click(date_picker: MDDockedDatePicker):
            date_picker.dismiss()

            date = date_picker.get_date()[0]

            self.ids.task_expire_date.text = date.strftime('%d.%m.%Y')

        if not focus:
            return

        date_dialog = MDDockedDatePicker()
        date_dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        date_dialog.bind(on_ok=on_ok_click)
        date_dialog.open()


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
