# pylint: disable=no-name-in-module
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QComboBox,
    QSpinBox,
)
from widgets.base_edit_form_widget import BaseEditFormWidget


class ServiceEditFormWidget(BaseEditFormWidget):
    def __init__(self) -> None:
        self.labels = [
            "Service Name",
            "Service Type",
            "Client",
            "Items Count",
        ]
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        super().initUI()

        # Create and add control widgets
        self.control_widgets = {}
        for label in self.labels:
            match label:
                case "Service Name":
                    widget = QLineEdit()
                case "Service Type":
                    widget = QComboBox()
                case "Client":
                    widget = QComboBox()
                case "Items Count":
                    widget = QSpinBox()
                case _:
                    raise ValueError(f"Invalid Service edit label: {label}")

            self.form_layout.addRow(f"{label}:", widget)
            self.control_widgets[label] = widget

        # Create and add specific buttons
        self.receive_button = QPushButton("Receive Item(s)")
        self.return_button = QPushButton("Return Item(s)")

        self.buttons_layout.addWidget(self.receive_button)
        self.buttons_layout.addWidget(self.return_button)

    def populate_edit_controls(self) -> None:
        pass
