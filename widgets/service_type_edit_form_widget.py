import copy
from typing import Optional, Dict, Any

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QIntValidator

from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.service_type import ServiceType
from entities.general_dict import GeneralDict


class ServiceTypeEditFormWidget(BaseEditFormWidget):
    def __init__(self) -> None:
        self._service_type: Optional[ServiceType] = None
        self.labels = {
            "Name": True,
            "Type": True,
            "Price": True,
        }
        super().__init__()

    def initUI(self) -> None:
        super().initUI()
        # Create and add control widgets
        self.control_widgets = {}
        for label, required in self.labels.items():
            widget = QLineEdit()
            match label:
                case "Name":
                    widget.setPlaceholderText("Enter service name (mandatory)")
                case "Type":
                    widget.setPlaceholderText("Enter service type (mandatory)")
                case "Price":
                    # Setup Price control value validator to force double values only
                    validator = QIntValidator(1, 100000)

                    widget.setPlaceholderText(
                        "Enter service price (mandatory). From 1 to 100 000"
                    )
                    widget.setValidator(validator)
                    widget.setText("1")
                case _:
                    raise ValueError(f"Invalid ServiceType edit label: {label}")

            self.form_layout.addRow(f"{label}: *" if required else label, widget)
            self.control_widgets[label] = widget

    def pre_populate_edit_controls(self, kwargs: Dict[str, GeneralDict]) -> None:
        pass

    def populate_edit_controls(self, item: ServiceType) -> None:
        # Copy ServiceType to remove Model ServiceTypetDict item reference
        self._service_type = copy.deepcopy(item)
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Type"].setText(item.type)
        self.control_widgets["Price"].setText(str(item.price))

    def set_enabled_edit_controls(self) -> None:
        pass

    def clear_edit_controls(self) -> None:
        self._service_type = None
        self.control_widgets["Name"].setText("")
        self.control_widgets["Type"].setText("")
        self.control_widgets["Price"].setText("1")

    def on_add_button_clicked(self) -> None:
        validation_message = self.validate_control_values()
        if not validation_message is None:
            QMessageBox.warning(self, "Failed to add Service Type", validation_message)
            return

        self._service_type = None
        service_type = ServiceType(
            code=None,
            name=self.control_widgets["Name"].text(),
            type=self.control_widgets["Type"].text(),
            price=int(self.control_widgets["Price"].text()),
        )

        self.add_button_signal.emit(service_type)

    def on_update_button_clicked(self) -> None:
        if self._service_type is None:
            QMessageBox.warning(
                self, "Failed to update Service Type", "Service Type is not selected"
            )
            return

        validation_message = self.validate_control_values()
        if not validation_message is None:
            QMessageBox.warning(
                self, "Failed to update Service Type", validation_message
            )
            return

        self._service_type.name = self.control_widgets["Name"].text()
        self._service_type.type = self.control_widgets["Type"].text()
        self._service_type.price = int(self.control_widgets["Price"].text())

        self.update_button_signal.emit(self._service_type)

    def on_clear_button_clicked(self) -> None:
        self.clear_edit_controls()

    def on_delete_button_clicked(self) -> None:
        if self._service_type is None or self._service_type.code is None:
            QMessageBox.warning(
                self, "Failed to delete Service Type", "Service Type is not selected"
            )
            return

        self.delete_button_signal.emit(self._service_type.code)

    def validate_control_values(self) -> str | None:
        message_parts = []
        value = ""
        message = ""
        for label, required in self.labels.items():
            if not required:
                continue
            message = f"'{label}' value cannot be empty"
            value = self.control_widgets[label].text().strip()

            def append_message(val: Any, msg: str) -> None:
                if val is None or val == "" or self.is_zero(val):
                    message_parts.append(msg)

            match label:
                case "Name" | "Type":
                    append_message(value, message)
                case "Price":
                    message = f"'{label}' value cannot be empty or 0"
                    append_message(value, message)

        return "\n".join(message_parts) if len(message_parts) > 0 else None

    def is_zero(self, val: Any) -> bool:
        try:
            int_val = int(val)
            return int_val == 0
        except ValueError:
            return False
