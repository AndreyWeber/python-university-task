import copy
from typing import Optional, Dict

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
from entities.general_dict import GeneralDict


class ServiceEditFormWidget(BaseEditFormWidget):
    receive_button_signal = pyqtSignal()
    return_button_signal = pyqtSignal()

    def __init__(self) -> None:
        self._service: Optional[Service] = None
        self._service_types: dict = {}
        self._clients: dict = {}
        self.labels = {
            "Service Name": True,
            "Service Type": True,
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
                    widget = QLineEdit()
                    widget.setPlaceholderText("Entel service name (mandatory)")
                case "Service Type":
                    widget = QComboBox()
                case "Client":
                    widget = QComboBox()
                case "Items Count":
                    widget = QSpinBox()
                    widget.setMinimum(1)
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

    def populate_edit_controls(
        self, item: Service, kwargs: Dict[str, GeneralDict]
    ) -> None:
        self.control_widgets["Service Name"].setText(item.service_type.name)
        self.control_widgets["Items Count"].setValue(item.items_count)
        self.populate_combobox(
            self.control_widgets["Service Type"],
            kwargs,
            "service_types",
            item.service_type.code,
        )
        self.populate_combobox(
            self.control_widgets["Client"], kwargs, "clients", item.client.code
        )
        #! TODO: Add buttons disabling and showing a warning

    def populate_combobox(
        self, combobox: QComboBox, items: dict, name: str, selected_code: int
    ) -> None:
        def combobox_data_to_dict(cbox: QComboBox) -> dict:
            return {cbox.itemText(i): cbox.itemData(i) for i in range(cbox.count())}

        combobox_new_data = {
            str(item): code for code, item in items.get(name, {}).items()
        }
        if combobox_data_to_dict(combobox) != combobox_new_data:
            combobox.clear()
            for text, data in combobox_new_data.items():
                combobox.addItem(text, data)

        current_idx = combobox.findData(selected_code)
        combobox.setCurrentIndex(current_idx)

    def clear_edit_controls(self) -> None:
        self._service = None

    def on_add_button_clicked(self) -> None:
        pass

    def on_update_button_clicked(self) -> None:
        pass

    def on_clear_button_clicked(self) -> None:
        self.clear_edit_controls()

    def on_delete_button_clicked(self) -> None:
        pass
