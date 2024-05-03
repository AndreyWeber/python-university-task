# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import pyqtSignal
from widgets.service_table_widget import ServiceTableWidget
from widgets.service_edit_form_widget import ServiceEditFormWidget
from entities.service_dict import ServiceDict


class ServiceTabWidget(QWidget):
    populate_service_table_signal = pyqtSignal(ServiceDict)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.service_table_widget = ServiceTableWidget()

        self.layout.addWidget(self.service_table_widget)

        self.populate_service_table_signal.connect(
            self.service_table_widget.populate_table
        )

        self.service_edit_form_widget = ServiceEditFormWidget()

        self.layout.addWidget(self.service_edit_form_widget)

        # bind populate edit controls

    def populate_table(self, services: ServiceDict):
        self.populate_service_table_signal.emit(services)
