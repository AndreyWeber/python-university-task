# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import pyqtSignal
from widgets.service_table_widget import ServiceTableWidget
from widgets.service_edit_form_widget import ServiceEditFormWidget
from entities.service_dict import ServiceDict
from entities.service import Service


class ServiceTabWidget(QWidget):
    populate_service_table_signal = pyqtSignal(ServiceDict)
    populate_service_edit_controls = pyqtSignal(Service)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.service_table_widget = ServiceTableWidget()
        self.service_edit_form_widget = ServiceEditFormWidget()

        self.populate_service_table_signal.connect(
            self.service_table_widget.populate_table
        )
        self.populate_service_edit_controls.connect(
            self.service_edit_form_widget.populate_edit_controls
        )

        self.layout.addWidget(self.service_table_widget)
        self.layout.addWidget(self.service_edit_form_widget)

        # bind populate edit controls

    def populate_table(self, services: ServiceDict) -> None:
        if not services:
            return
        self.populate_service_table_signal.emit(services)

    def populate_edit_controls(self, service: Service) -> None:
        if not service:
            return
        self.populate_service_edit_controls.emit(service)

    def get_code_value(self, row_index: int) -> int:
        return self.service_table_widget.get_code_value(row_index)
