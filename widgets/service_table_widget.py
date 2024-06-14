import logging

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QTableWidgetItem
from widgets.base_table_widget import BaseTableWidget
from entities.service_dict import ServiceDict


class ServiceTableWidget(BaseTableWidget):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

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

    def populate_table(self, items_dict: ServiceDict) -> None:
        values = items_dict.values()
        self.table.setRowCount(len(values))

        for row, service in enumerate(values):
            self.table.setItem(row, 0, QTableWidgetItem(str(service.code)))
            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    "N/A" if service.service_type is None else service.service_type.name
                ),
            )
            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    "N/A" if service.service_type is None else service.service_type.type
                ),
            )
            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    "N/A" if service.client is None else str(service.client)
                ),
            )
            self.table.setItem(row, 4, QTableWidgetItem(str(service.items_count)))
            self.table.setItem(
                row, 5, QTableWidgetItem(str(self.try_get_service_cost(service)))
            )
            self.table.setItem(
                row,
                6,
                QTableWidgetItem(
                    service.date_received.strftime("%d.%m.%Y")
                    if service.date_received
                    else "N/A"
                ),
            )
            self.table.setItem(
                row,
                7,
                QTableWidgetItem(
                    service.date_returned.strftime("%d.%m.%Y")
                    if service.date_returned
                    else "N/A"
                ),
            )

        super().populate_table(items_dict)

    def try_get_service_cost(self, service) -> float:
        try:
            return service.calculate_cost()
        except ValueError as e:
            self.logger.error("Failed to calculate Service Price: '%s'", e)
            return 0.0
