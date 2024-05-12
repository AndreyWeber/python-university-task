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
                    widget.setPlaceholderText("Enter service name (mandatory)")
                case "Type":
                    widget = QLineEdit()
                    widget.setPlaceholderText("Enter service type (mandatory)")
                case "Price":
                    #! TODO: Check if there is a more suitable control
                    widget = QLineEdit()
                    widget.setPlaceholderText(
                        "Enter service price (mandatory). From 1.00 to 100 000.00"
                    )
                case _:
                    raise ValueError(f"Invalid ServiceType edit label: {label}")

            self.form_layout.addRow(f"{label}:", widget)
            self.control_widgets[label] = widget

    def populate_edit_controls(self, item: ServiceType) -> None:
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Type"].setText(item.type)
        self.control_widgets["Price"].setText(str(item.price))

    def on_add_button_clicked(self) -> None:
        pass

    def on_update_button_clicked(self) -> None:
        pass

    def on_clear_button_clicked(self) -> None:
        pass

    def on_delete_button_clicked(self) -> None:
        pass
