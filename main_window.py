# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
from dry_cleaning import DryCleaning


class MainWindow(QMainWindow):
    def __init__(self, dry_cleaning: DryCleaning):
        super().__init__()
        self.__dry_cleaning = dry_cleaning
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle("Dry Cleaning")
        self.setGeometry(100, 100, 800, 400)

        # Create a table
        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            [
                "Code",
                "Service Type",
                "Client",
                "Items Count",
                "Date Received",
                "Date Returned",
            ]
        )

        # Populate the table
        self.populate_table()

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def populate_table(self):
        services = self.__dry_cleaning.services.item_dict.values()
        self.table.setRowCount(len(services))

        for row, service in enumerate(services):
            self.table.setItem(row, 0, QTableWidgetItem(str(service.code)))
            self.table.setItem(row, 1, QTableWidgetItem(service.service_type.name))
            self.table.setItem(row, 2, QTableWidgetItem(service.client.name))
            self.table.setItem(row, 3, QTableWidgetItem(service.items_count))
            self.table.setItem(
                row, 4, QTableWidgetItem(service.date_received.strftime("%d.%m.%Y"))
            )
            self.table.setItem(
                row,
                5,
                QTableWidgetItem(
                    service.date_returned.strftime("%d.%m.%Y")
                    if service.date_returned
                    else ""
                ),
            )

        self.table.cellClicked.connect(self.on_cell_clicked)

    def on_cell_clicked(self, row, column) -> None:
        print(f"Cell {row}, {column} clicked")
