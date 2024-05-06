# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QLineEdit,
)
from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.service_type import ServiceType


class ServiceTypeEditFormWidget(BaseEditFormWidget):
    def __init__(self) -> None:
        self.labels = [
            "Name",
            "Type",
            "Price",
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
                case "Type":
                    widget = QLineEdit()
                case "Price":
                    #! TODO: Check if there is a more suitable control
                    widget = QLineEdit()
                    widget.setText("0")
                case _:
                    raise ValueError(f"Invalid Service edit label: {label}")

            self.form_layout.addRow(f"{label}:", widget)
            self.control_widgets[label] = widget

    def populate_edit_controls(self, item: ServiceType) -> None:
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Type"].setText(item.type)
        self.control_widgets["Price"].setText(str(item.price))
