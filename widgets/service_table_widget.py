# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QTableWidgetItem
from widgets.base_table_widget import BaseTableWidget
from entities.service_dict import ServiceDict


class ServiceTableWidget(BaseTableWidget):
    def __init__(self):
        headers = [
            "Code",
            "Service Name",
            "Service Type",
            "Client Name",
            "Items Count",
            "Total Cost",
            "Date Received",
            "Date Returned",
        ]
        super().__init__(headers)

    def populate_table(self, services: ServiceDict):
        services = services.item_dict.values()
        self.table.setRowCount(len(services))

        for row, service in enumerate(services):
            self.table.setItem(row, 0, QTableWidgetItem(str(service.code)))
            self.table.setItem(row, 1, QTableWidgetItem(service.service_type.name))
            self.table.setItem(row, 2, QTableWidgetItem(service.service_type.type))
            self.table.setItem(row, 3, QTableWidgetItem(str(service.client)))
            self.table.setItem(row, 4, QTableWidgetItem(str(service.items_count)))
            self.table.setItem(row, 5, QTableWidgetItem(str(service.calculate_cost())))
            self.table.setItem(
                row, 6, QTableWidgetItem(service.date_received.strftime("%d.%m.%Y"))
            )
            self.table.setItem(
                row,
                7,
                QTableWidgetItem(
                    service.date_returned.strftime("%d.%m.%Y")
                    if service.date_returned
                    else ""
                ),
            )
