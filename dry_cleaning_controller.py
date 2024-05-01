from dry_cleaning_view import DryCleaningView
from dry_cleaning import DryCleaning


class DryCleaningController:
    def __init__(self, model: DryCleaning, view: DryCleaningView):
        self.model = model
        self.view = view

        # Connect signals to slots
        self.view.load_xml_data_signal.connect(self.load_xml_data)
        self.view.load_sqlite_data_signal.connect(self.load_sqlite_data)
        self.view.save_xml_data_signal.connect(self.save_xml_data)
        self.view.save_sqlite_data_signal.connect(self.save_sqlite_data)

        # Populate initial data
        self.populate_tabs()

    def populate_tabs(self):
        services = self.model.services
        self.view.tabs.widget(0).populate_table(services)

    def load_xml_data(self):
        pass

    def load_sqlite_data(self):
        pass

    def save_xml_data(self):
        pass

    def save_sqlite_data(self):
        pass

    def populate_table(self):
        pass

    def adjust_columns_size(self):
        pass

    def adjust_window_size(self):
        pass

    def on_cell_clicked(self, index):
        pass

    def on_row_header_clicked(self, index):
        pass

    def load_data_into_edits(self, row):
        pass

    def on_save_changes_clicked(self):
        pass


# class DryCleaningView(QMainWindow):
#     def __init__(self, dry_cleaning: DryCleaning):
#         super().__init__()
#         self._dry_cleaning = dry_cleaning
#         self.initUI()

#     def initUI(self) -> None:
#         self.setWindowTitle("Dry Cleaning Management")
#         self.setGeometry(100, 100, 800, 600)

#         # Layout setup
#         layout = QVBoxLayout()

#         # Table setup
#         self.table = QTableWidget(self)
#         self.table.setColumnCount(6)
#         self.table.setHorizontalHeaderLabels(
#             [
#                 "Code",
#                 "Service Type",
#                 "Client",
#                 "Items Count",
#                 "Date Received",
#                 "Date Returned",
#             ]
#         )
#         self.table.clicked.connect(self.on_cell_clicked)
#         self.table.verticalHeader().sectionClicked.connect(self.on_row_header_clicked)
#         layout.addWidget(self.table)

#         # Edit controls
#         self.edit_code = QLineEdit(self)
#         self.edit_service_type = QLineEdit(self)
#         self.edit_client = QLineEdit(self)
#         self.items_count = QLineEdit(self)
#         self.date_received = QDateEdit(self)
#         self.date_returned = QDateEdit(self)
#         self.submit_button = QPushButton("Save", self)
#         self.submit_button.clicked.connect(self.on_save_changes_clicked)

#         # Adding edit controls to layout
#         h_layout = QHBoxLayout()
#         h_layout.addWidget(QLabel("Code:", self))
#         h_layout.addWidget(self.edit_code)
#         self.edit_code.setMaximumWidth(200)

#         # layout.addWidget(self.edit_code)
#         layout.addLayout(h_layout)

#         layout.addWidget(self.edit_service_type)
#         layout.addWidget(self.edit_client)
#         layout.addWidget(self.items_count)
#         layout.addWidget(self.date_received)
#         layout.addWidget(self.date_returned)
#         layout.addWidget(self.submit_button)

#         # Central widget
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Populate the table
#         self.populate_table()

#         # Adjust columns and window size
#         self.adjust_columns_size()
#         self.adjust_window_size()

#     def populate_table(self):
#         services = self._dry_cleaning.services.item_dict.values()
#         self.table.setRowCount(len(services))

#         for row, service in enumerate(services):
#             self.table.setItem(row, 0, QTableWidgetItem(str(service.code)))
#             self.table.setItem(row, 1, QTableWidgetItem(service.service_type.name))
#             self.table.setItem(row, 2, QTableWidgetItem(str(service.client)))
#             self.table.setItem(row, 3, QTableWidgetItem(service.items_count))
#             self.table.setItem(
#                 row, 4, QTableWidgetItem(service.date_received.strftime("%d.%m.%Y"))
#             )
#             self.table.setItem(
#                 row,
#                 5,
#                 QTableWidgetItem(
#                     service.date_returned.strftime("%d.%m.%Y")
#                     if service.date_returned
#                     else ""
#                 ),
#             )

#     def adjust_columns_size(self) -> None:
#         self.table.resizeColumnsToContents()
#         for col in range(self.table.columnCount()):
#             margined_width = self.table.columnWidth(col) + 5
#             self.table.setColumnWidth(col, margined_width)

#     def adjust_window_size(self) -> None:
#         width = self.table.verticalHeader().width() + 45
#         width += self.table.horizontalHeader().length()
#         if self.table.verticalScrollBar().isVisible():
#             width += self.table.verticalScrollBar().width()
#         width += self.table.frameWidth() * 2

#         height = self.geometry().height()

#         self.setGeometry(100, 100, width, height)

#     def on_cell_clicked(self, index) -> None:
#         row = index.row()
#         column = index.column()
#         print(f"Cell {row}, {column} clicked")
#         self.load_data_into_edits(row)

#     def on_row_header_clicked(self, index) -> None:
#         self.load_data_into_edits(index)

#     def on_save_changes_clicked(self) -> None:
#         pass

#     def load_data_into_edits(self, row: int) -> None:
#         item = self.table.item(row, 0)
#         if item is None:
#             self.edit_code.clear()
#         else:
#             code = item.text()
#             service = self._dry_cleaning.services.item_dict[int(code)]
#             self.edit_code.setText(code)
#             self.date_received.setDate(service.date_received)
