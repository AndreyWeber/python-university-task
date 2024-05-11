# pylint: disable=no-name-in-module
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QComboBox,
    QSpinBox,
)
from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.service import Service


class ServiceEditFormWidget(BaseEditFormWidget):
    receive_button_signal = pyqtSignal()
    return_button_signal = pyqtSignal()

    def __init__(self) -> None:
        self.labels = [
            "Service Name",
            "Service Type",
            "Client",
            "Items Count",
        ]
        super().__init__()

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
                    widget.setMinimum(0)
                case _:
                    raise ValueError(f"Invalid Service edit label: {label}")

            self.form_layout.addRow(f"{label}:", widget)
            self.control_widgets[label] = widget

        # Create and add specific buttons
        self.receive_button = QPushButton("Receive Item(s)")
        self.return_button = QPushButton("Return Item(s)")

        self.receive_button.clicked.connect(self.receive_button_signal.emit)
        self.return_button.clicked.connect(self.return_button_signal.emit)

        self.buttons_layout.addWidget(self.receive_button)
        self.buttons_layout.addWidget(self.return_button)

    def populate_edit_controls(self, item: Service) -> None:
        self.control_widgets["Service Name"].setText(item.service_type.name)
        self.control_widgets["Items Count"].setValue(item.items_count)

    def on_add_button_clicked(self) -> None:
        pass

    def on_update_button_clicked(self) -> None:
        pass

    def on_clear_button_clicked(self) -> None:
        pass

    def on_delete_button_clicked(self) -> None:
        pass
