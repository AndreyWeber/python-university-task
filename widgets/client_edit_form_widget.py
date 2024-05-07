# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QLineEdit,
    QCheckBox,
)
from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.client import Client


class ClientEditFormWidget(BaseEditFormWidget):
    def __init__(self) -> None:
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
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Surname"].setText(item.surname)
        self.control_widgets["Second Name"].setText(item.second_name)
        self.control_widgets["Is Regular"].setChecked(item.is_regular)
