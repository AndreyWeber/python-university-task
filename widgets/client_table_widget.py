# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QTableWidgetItem
from widgets.base_table_widget import BaseTableWidget
from entities.client_dict import ClientDict


class ClientTableWidget(BaseTableWidget):
    def __init__(self):
        headers = [
            "Code",
            "Name",
            "Surname",
            "Second Name",
            "Is Regular",
        ]
        super().__init__(headers)

    def populate_table(self, items_dict: ClientDict) -> None:
        values = items_dict.values()
        self.table.setRowCount(len(values))

        for row, client in enumerate(values):
            self.table.setItem(row, 0, QTableWidgetItem(str(client.code)))
            self.table.setItem(row, 1, QTableWidgetItem(client.name))
            self.table.setItem(row, 2, QTableWidgetItem(client.surname))
            self.table.setItem(row, 3, QTableWidgetItem(client.second_name))
            self.table.setItem(row, 4, QTableWidgetItem(str(client.is_regular)))
