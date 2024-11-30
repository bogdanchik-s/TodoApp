from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemHeadlineText,
    MDListItemSupportingText,
    MDListItemTertiaryText,
    MDListItemTrailingIcon
)
from kivy.metrics import dp

from View.base_screen import BaseScreenView
from Model.database import Task


class MainScreenView(BaseScreenView):
    def on_pre_enter(self):
        self.controller.load_tasks()

    def add_task(self, task: Task):
        task_list_item = MDListItem(
            MDListItemLeadingIcon(icon='clipboard-clock-outline'),
            MDListItemHeadlineText(text=task.title),
            MDListItemSupportingText(text=task.description),
            MDListItemTertiaryText(text=f'Выполнить до: {task.expire_date}'),
            MDListItemTrailingIcon(icon='trash-can-outline'),
            id=f'task_{task.id}',
            on_release=self.delete_task
        )

        self.ids.task_list.add_widget(task_list_item)

    def delete_task(self, task_list_item: MDListItem):
        self.ids.task_list.remove_widget(task_list_item)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        if len(self.model.tasks) > 0:
            for task in self.model.tasks:
                self.add_task(task)
