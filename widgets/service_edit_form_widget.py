import logging
import sys
from typing import Optional, Dict

# pylint: disable=no-name-in-module
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QPushButton,
    QComboBox,
    QSpinBox,
    QMessageBox,
)
from widgets.base_edit_form_widget import BaseEditFormWidget
from widgets.gray_out_delegate import GrayOutDelegate
from entities.service import Service
from entities.client import Client
from entities.service_type import ServiceType
from entities.general_dict import GeneralDict


class ServiceEditFormWidget(BaseEditFormWidget):
    receive_button_signal = pyqtSignal()
    return_button_signal = pyqtSignal()

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

        self._service: Optional[Service] = None
        self._service_types: dict = {}
        self._clients: dict = {}
        self.labels = {
            "Service Name": True,
            "Client": True,
            "Items Count": True,
        }
        super().__init__()

    def initUI(self) -> None:
        super().initUI()
        # Create and add control widgets
        self.control_widgets = {}
        for label, required in self.labels.items():
            match label:
                case "Service Name":
                    widget = QComboBox()
                case "Client":
                    widget = QComboBox()
                case "Items Count":
                    widget = QSpinBox()
                    widget.setMinimum(1)
                    widget.setMaximum(100)
                case _:
                    raise ValueError(f"Invalid Service edit label: {label}")

            self.form_layout.addRow(f"{label}: *" if required else f"{label}:", widget)
            self.control_widgets[label] = widget

        # Create and add specific buttons
        self.receive_button = QPushButton("Receive Item(s)")
        self.return_button = QPushButton("Return Item(s)")

        self.receive_button.clicked.connect(self.receive_button_signal.emit)
        self.return_button.clicked.connect(self.return_button_signal.emit)

        self.buttons_layout.addWidget(self.receive_button)
        self.buttons_layout.addWidget(self.return_button)

    def pre_populate_edit_controls(self, kwargs: Dict[str, GeneralDict]) -> None:
        self.populate_combobox(
            self.control_widgets["Service Name"],
            kwargs.get("service_types", {}),
            None,
            "Select Service Name...",
        )
        self.populate_combobox(
            self.control_widgets["Client"],
            kwargs.get("clients", {}),
            None,
            "Select Client...",
        )

    def populate_edit_controls(self, item: Service) -> None:
        self.control_widgets["Items Count"].setValue(item.items_count)
        self.set_combobox_selected_or_default_item(
            self.control_widgets["Service Name"],
            None if item.service_type is None else item.service_type.code,
        )
        self.set_combobox_selected_or_default_item(
            self.control_widgets["Client"],
            None if item.client is None else item.client.code,
        )

    #! TODO: Add buttons disabling and showing a warning

    def clear_edit_controls(self) -> None:
        self._service = None
        self.set_combobox_selected_or_default_item(
            self.control_widgets["Service Name"], None
        )
        self.set_combobox_selected_or_default_item(self.control_widgets["Client"], None)
        self.control_widgets["Items Count"].setValue(1)

    def on_add_button_clicked(self) -> None:
        validation_message = self.validate_control_values()
        if not validation_message is None:
            QMessageBox.warning(self, "Failed to add Service", validation_message)
            return

        client_code = self.control_widgets["Client"].currentData()
        service_type_code = self.control_widgets["Service Name"].currentData()

        self._service = None
        service = Service(
            code=None,
            date_received=None,
            date_returned=None,
            items_count=self.control_widgets["Items Count"].value(),
            client=Client(code=client_code),
            service_type=ServiceType(code=service_type_code),
        )

        self.add_button_signal.emit(service)

    def on_update_button_clicked(self) -> None:
        pass

    def on_clear_button_clicked(self) -> None:
        self.clear_edit_controls()

    def on_delete_button_clicked(self) -> None:
        pass

    #! TODO: Add default value with placeholder
    def populate_combobox(
        self,
        combobox: QComboBox,
        items_dict: dict,
        selected_code: int | None,
        placeholder_text: str,
    ) -> None:
        def combobox_data_to_dict(cbox: QComboBox) -> dict:
            return {cbox.itemText(i): cbox.itemData(i) for i in range(cbox.count())}

        combobox_old_data = combobox_data_to_dict(combobox)
        combobox_new_data = {str(item): code for code, item in items_dict.items()}
        if combobox_old_data != combobox_new_data or (
            not combobox_old_data and not combobox_new_data
        ):
            # Clear combobox items if there were any
            if combobox_old_data:
                combobox.clear()
            # Add placeholder
            combobox.addItem(placeholder_text, sys.maxsize)
            # Add data if data is not empty
            for text, data in combobox_new_data.items() if combobox_new_data else {}:
                combobox.addItem(text, data)

        self.set_combobox_selected_or_default_item(combobox, selected_code)

        combobox.setItemDelegate(GrayOutDelegate())

    def set_combobox_selected_or_default_item(
        self, combobox: QComboBox, selected_code: int | None
    ) -> None:
        idx_to_set = combobox.findData(
            sys.maxsize if selected_code is None else selected_code
        )
        # Set combobox item if index was found or log message if not
        if idx_to_set == -1:
            logging.info(
                "Failed to select item by code '%s' for combobox '%s'",
                selected_code,
                combobox,
            )
        else:
            combobox.setCurrentIndex(idx_to_set)

    def validate_control_values(self) -> str | None:
        message_parts = []
        for label, required in self.labels.items():
            if not required:
                continue
            if label != "Service Name" and label != "Client":
                continue
            data = self.control_widgets[label].currentData()
            if data == sys.maxsize:
                message_parts.append(f"Please select '{label}' non-default value")

        return "\n".join(message_parts) if len(message_parts) > 0 else None
