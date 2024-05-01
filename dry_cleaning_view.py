# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTabWidget,
    QMenuBar,
    QAction,
)
from PyQt5.QtCore import pyqtSignal
from service_tab import ServiceTab


class DryCleaningView(QMainWindow):
    load_xml_data_signal = pyqtSignal()
    load_sqlite_data_signal = pyqtSignal()
    save_xml_data_signal = pyqtSignal()
    save_sqlite_data_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle("Dry Cleaning Management")
        self.setGeometry(100, 100, 1100, 600)

        # Central widget and main layout
        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)

        # Top menu bar setup
        self.create_menu_bar()

        # Tabs setup
        self.tabs = QTabWidget()

        self.tabs.addTab(ServiceTab(), "Services")
        # self.tabs.addTab(ServiceTypesTab(), "Service Types")
        # self.tabs.addTab(ClientsTab(), "Clients")
        self.tabs.addTab(QWidget(), "Service Types")
        self.tabs.addTab(QWidget(), "Clients")

        main_layout.addWidget(self.tabs)

        self.setCentralWidget(central_widget)

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)

        file_menu = menu_bar.addMenu("File")

        load_xml_action = QAction("Load XML", self)
        load_sqlite_action = QAction("Load SQLite", self)
        save_xml_action = QAction("Save XML", self)
        save_sqlite_action = QAction("Save SQLite", self)

        load_xml_action.triggered.connect(self.load_xml_data_signal.emit)
        load_sqlite_action.triggered.connect(self.load_sqlite_data_signal.emit)
        save_xml_action.triggered.connect(self.save_xml_data_signal.emit)
        save_sqlite_action.triggered.connect(self.save_sqlite_data_signal.emit)

        file_menu.addAction(load_xml_action)
        file_menu.addAction(load_sqlite_action)
        file_menu.addSeparator()
        file_menu.addAction(save_xml_action)
        file_menu.addAction(save_sqlite_action)

        self.setMenuBar(menu_bar)
