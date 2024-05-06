# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QTableWidgetItem
from widgets.base_table_widget import BaseTableWidget
from entities.service_type_dict import ServiceTypeDict


class ServiceTypeTableWidget(BaseTableWidget):
    def __init__(self):
        headers = [
            "Code",
            "Name",
            "Type",
            "Price",
        ]
        super().__init__(headers)

    def populate_table(self, items_dict: ServiceTypeDict) -> None:
        values = items_dict.values()
        self.table.setRowCount(len(values))

        for row, service_type in enumerate(values):
            self.table.setItem(row, 0, QTableWidgetItem(str(service_type.code)))
            self.table.setItem(row, 1, QTableWidgetItem(service_type.name))
            self.table.setItem(row, 2, QTableWidgetItem(service_type.type))
            self.table.setItem(row, 3, QTableWidgetItem(str(service_type.price)))
