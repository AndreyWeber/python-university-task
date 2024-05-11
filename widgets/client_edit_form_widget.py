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
            "Is Regular" : False,
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
                case "Surname":
                    widget = QLineEdit()
                case "Second Name":
                    widget = QLineEdit()
                case "Is Regular":
                    widget = QCheckBox()
                case _:
                    raise ValueError(f"Invalid Client edit label: {label}")

            self.form_layout.addRow(
                f"{label}: *" if required else label, widget
            )
            self.control_widgets[label] = widget

    def populate_edit_controls(self, item: Client) -> None:
        # Copy Client to remove Model ClientDict item reference
        self._client = copy.deepcopy(item)
        self.control_widgets["Name"].setText(item.name)
        self.control_widgets["Surname"].setText(item.surname)
        self.control_widgets["Second Name"].setText(item.second_name)
        self.control_widgets["Is Regular"].setChecked(item.is_regular)

    def on_add_button_clicked(self) -> None:
        self._client = None
        client = Client(
            code = None,
            name = self.control_widgets["Name"].text(),
            surname = self.control_widgets["Surname"].text(),
            second_name = self.control_widgets["Second Name"].text(),
            is_regular = self.control_widgets["Is Regular"].isChecked()
        )

        self.add_button_signal.emit(client)

    def on_save_button_clicked(self) -> None:
        if self._client is None:
            warning = "Client is not selected"
            QMessageBox.warning(self, "Failed to save", warning)
            self.logger.warning(warning)
            return
        self._client.name = self.control_widgets["Name"].text()
        self._client.surname = self.control_widgets["Surname"].text()
        self._client.second_name = self.control_widgets["Second Name"].text()
        self._client.is_regular = self.control_widgets["Is Regular"].isChecked()

        self.save_button_signal.emit(self._client)

    def on_clear_button_clicked(self) -> None:
        self._client = None
        self.control_widgets["Name"].setText("")
        self.control_widgets["Surname"].setText("")
        self.control_widgets["Second Name"].setText("")
        self.control_widgets["Is Regular"].setChecked(False)

    def on_delete_button_clicked(self) -> None:
        if self._client is None or self._client.code is None:
            warning = "Client is not selected"
            QMessageBox.warning(self, "Failed to delete", warning)
            self.logger.warning(warning)
            return

        self.delete_button_signal.emit(self._client.code)
