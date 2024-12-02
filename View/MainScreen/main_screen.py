from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemHeadlineText,
    MDListItemSupportingText,
    MDListItemTertiaryText,
    MDListItemTrailingCheckbox
)
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.metrics import dp

from View.base_screen import BaseScreenView
from Model.database import Task


class MainScreenView(BaseScreenView):

    def on_pre_enter(self):
        self.add_task_button = self.ids.actions_bar.ids.root_box.children[0].children[2]
        self.edit_task_button = self.ids.actions_bar.ids.root_box.children[0].children[1]
        self.delete_task_button = self.ids.actions_bar.ids.root_box.children[0].children[0]
        
        self.ids.tasks_list.clear_widgets()
        self.controller.load_tasks()

    def add_task(self, task: Task):
        task_list_item = MDListItem(
            MDListItemLeadingIcon(icon='clipboard-clock-outline'),
            MDListItemHeadlineText(text=task.title),
            MDListItemSupportingText(text=task.description),
            MDListItemTertiaryText(text=f'Выполнить до: {task.expire_date}'),
            MDListItemTrailingCheckbox(on_release=self.select_task),
            id=f'task_{task.id}',
            radius=5,
            ripple_effect=False
        )

        self.ids.tasks_list.add_widget(task_list_item)

    def select_task(self, _):
        selected_tasks_exist = False

        for task_item in self.ids.tasks_list.children:
            task_checkbox = task_item.children[0].children[0]

            if task_checkbox.active:
                selected_tasks_exist = True

        self.delete_task_button.disabled = not selected_tasks_exist

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        if len(self.model.tasks) > 0:
            for task in self.model.tasks:
                self.add_task(task)
