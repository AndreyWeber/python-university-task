import logging
import copy
from typing import Optional

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QLineEdit,
    QCheckBox,
    QMessageBox,
)
from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.client import Client


class ClientEditFormWidget(BaseEditFormWidget):
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

        self._client: Optional[Client] = None
        self.labels = {
            "Name": True,
            "Surname": True,
            "Second Name": True,
            "Is Regular": False,
        }
        super().__init__()

    def initUI(self) -> None:
        super().initUI()
        # Create and add control widgets
        self.control_widgets = {}
        for label, required in self.labels.items():
            match label:
                case "Name":
                    widget = QLineEdit()
                    widget.setPlaceholderText("Enter client name (mandatory)")
                case "Surname":
                    widget = QLineEdit()
                    widget.setPlaceholderText("Enter client surname (mandatory)")
                case "Second Name":
                    widget = QLineEdit()
                    widget.setPlaceholderText("Enter client second name (mandatory)")
                case "Is Regular":
                    widget = QCheckBox()
                case _:
                    raise ValueError(f"Invalid Client edit label: {label}")

            self.form_layout.addRow(f"{label}: *" if required else label, widget)
            self.control_widgets[label] = widget

    def populate_edit_controls(self, item: Client) -> None:
        # Copy Client to remove Model ClientDict item reference
        self._client = copy.deepcopy(item)
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Surname"].setText(item.surname)
        self.control_widgets["Second Name"].setText(item.second_name)
        self.control_widgets["Is Regular"].setChecked(item.is_regular)

    def on_add_button_clicked(self) -> None:
        validation_message = self.validate_control_values()
        if not validation_message is None:
            QMessageBox.warning(self, "Failed to add Client", validation_message)
            return

        self._client = None
        client = Client(
            code=None,
            name=self.control_widgets["Name"].text(),
            surname=self.control_widgets["Surname"].text(),
            second_name=self.control_widgets["Second Name"].text(),
            is_regular=self.control_widgets["Is Regular"].isChecked(),
        )
        try:
            self.add_button_signal.emit(client)
        except ValueError as e:
            QMessageBox.critical(self, "Failed to add Client", e)

    def on_update_button_clicked(self) -> None:
        if self._client is None:
            QMessageBox.warning(
                self, "Failed to update Client", "Client is not selected"
            )
            return

        validation_message = self.validate_control_values()
        if not validation_message is None:
            QMessageBox.warning(self, "Failed to update Client", validation_message)
            return

        self._client.name = self.control_widgets["Name"].text()
        self._client.surname = self.control_widgets["Surname"].text()
        self._client.second_name = self.control_widgets["Second Name"].text()
        self._client.is_regular = self.control_widgets["Is Regular"].isChecked()

        self.update_button_signal.emit(self._client)

    def on_clear_button_clicked(self) -> None:
        self._client = None
        self.control_widgets["Name"].setText("")
        self.control_widgets["Surname"].setText("")
        self.control_widgets["Second Name"].setText("")
        self.control_widgets["Is Regular"].setChecked(False)

    def on_delete_button_clicked(self) -> None:
        if self._client is None or self._client.code is None:
            QMessageBox.warning(
                self, "Failed to delete Client", "Client is not selected"
            )
            return

        self.delete_button_signal.emit(self._client.code)

    def validate_control_values(self) -> str | None:
        message_parts = []
        value = ""
        message = ""
        for label, required in self.labels.items():
            if not required:
                continue
            message = f"'{label}' value cannot be empty"
            value = self.control_widgets[label].text().strip()

            def append_message() -> None:
                if value is None or value == "":
                    message_parts.append(message)

            match label:
                case "Name" | "Surname" | "Second Name":
                    append_message()

        return "\n".join(message_parts) if len(message_parts) > 0 else None
