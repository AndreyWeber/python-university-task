# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import pyqtSignal
from service_table_widget import ServiceTableWidget
from service_dict import ServiceDict


class ServiceTab(QWidget):
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

        #! TODO: add edit controls and buttons widget

    def populate_table(self, services: ServiceDict):
        self.populate_service_table_signal.emit(services)
