from pathlib import Path
from views.dry_cleaning_view import DryCleaningView
from models.dry_cleaning import DryCleaning
from api.base_data_handler import BaseDataHandler
from api.xml_data_handler import XmlDataHandler


class DryCleaningController:
    def __init__(self, model: DryCleaning, view: DryCleaningView):
        self._model: DryCleaning = model
        self._view: DryCleaningView = view

        self._data_handler: BaseDataHandler = None

        # Connect signals to slots

        # Top menu signals
        self._view.load_xml_data_signal.connect(self.load_xml_data)
        self._view.load_sqlite_data_signal.connect(self.load_sqlite_data)
        self._view.save_xml_data_signal.connect(self.save_xml_data)
        self._view.save_sqlite_data_signal.connect(self.save_sqlite_data)

        # Service table signals
        #! TODO: self._view can store currently active tab index to use it in widget(0)
        svc_table_wdgt = self._view.tabs.widget(0).service_table_widget
        svc_table_wdgt.table_cell_clicked_signal.connect(self.on_cell_clicked)
        svc_table_wdgt.table_row_header_clicked_signal.connect(
            self.on_row_header_clicked
        )

        # Populate initial data
        self.populate_tabs()

    def populate_tabs(self):
        services = self._model.services
        self._view.tabs.widget(0).populate_table(services)

    def on_cell_clicked(self, cell_index) -> None:
        row_index = cell_index.row()
        code = self._view.tabs.widget(0).get_code_value(row_index)
        if not code:
            #! TODO: Would be good to add logging here
            return
        service = self._model.services.get(code, None)
        self._view.tabs.widget(0).populate_edit_controls(service)

    def on_row_header_clicked(self, row_index) -> None:
        print(f"Row {row_index} clicked")
        self._view.tabs.widget(0).populate_edit_controls(row_index)

    def populate_table(self):
        pass

    def adjust_columns_size(self):
        pass

    def adjust_window_size(self):
        pass

    def load_data_into_edits(self, row):
        pass

    def on_save_changes_clicked(self):
        pass

    # Top menu action handlers
    def load_xml_data(self):
        self._data_handler = XmlDataHandler(
            self._model,
            str(Path(".\\oldfile.xml").resolve()),
            str(Path(".\\newfile.xml").resolve()),
        )
        self._data_handler.read()
        self.populate_tabs()

    def load_sqlite_data(self):
        raise NotImplementedError("'load_sqlite_data()' not implemented")

    def save_xml_data(self):
        if not self._data_handler is None:
            self._data_handler.write()

    def save_sqlite_data(self):
        raise NotImplementedError("'save_sqlite_data()' not implemented")


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
