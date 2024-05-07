import logging
from typing import Optional
# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QLineEdit,
    QCheckBox,
)
from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.client import Client


class ClientEditFormWidget(BaseEditFormWidget):
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

        self._client: Optional[Client] = None
        self.labels = [
            "Name",
            "Surname",
            "Second Name",
            "Is Regular",
        ]
        super().__init__()

    def initUI(self) -> None:
        super().initUI()

        # Create and add control widgets
        self.control_widgets = {}
        for label in self.labels:
            match label:
                case "Name":
                    widget = QLineEdit()
                case "Surname":
                    widget = QLineEdit()
                case "Second Name":
                    widget = QLineEdit()
                case "Is Regular":
                    widget = QCheckBox()
                case _:
                    raise ValueError(f"Invalid Client edit label: {label}")

            self.form_layout.addRow(f"{label}:", widget)
            self.control_widgets[label] = widget

    def populate_edit_controls(self, item: Client) -> None:
        self._client = item
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Surname"].setText(item.surname)
        self.control_widgets["Second Name"].setText(item.second_name)
        self.control_widgets["Is Regular"].setChecked(item.is_regular)

    def on_save_button_clicked(self) -> None:
        self._client.name = self.control_widgets["Name"].text()
        self._client.surname = self.control_widgets["Surname"].text()
        self._client.second_name = self.control_widgets["Second Name"].text()
        self._client.second_name = self.control_widgets["Is Regular"].isChecked()

        self.save_button_signal.emit(self._client)

    def on_add_button_clicked(self) -> None:
        self.add_button_signal.emit(self._client)

    def on_delete_button_clicked(self) -> None:
        if self._client is None or self._client.code is None:
            self.logger.info("There is no client to delete or its code is not defined")
            return
        self.delete_button_signal.emit(self._client.code)
