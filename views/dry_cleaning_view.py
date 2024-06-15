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

from widgets.base_tab_widget import BaseTabWidget
from widgets.service_tab_widget import ServiceTabWidget
from widgets.service_type_tab_widget import ServiceTypeTabWidget
from widgets.client_tab_widget import ClientTabWidget

from api.handler_type import HandlerType


class DryCleaningView(QMainWindow):
    load_data_signal = pyqtSignal(HandlerType)
    save_data_signal = pyqtSignal(HandlerType)
    tab_changed_signal = pyqtSignal()
    window_width_changed_signal = pyqtSignal(int)

    default_tab_index: int = 0

    def __init__(self):
        super().__init__()
        self._max_window_width = 1100
        self._active_tab_index = self.default_tab_index
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle("Dry Cleaning Management")
        self.setGeometry(100, 100, self._max_window_width, 650)

        # Central widget and main layout
        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)

        # Top menu bar setup
        self.create_menu_bar()

        # Tabs setup
        self.tabs = QTabWidget()

        self.tabs.addTab(ServiceTabWidget(self), "Services")
        self.tabs.addTab(ServiceTypeTabWidget(self), "Service Types")
        self.tabs.addTab(ClientTabWidget(self), "Clients")

        # Connect the tab changed signal
        self.tabs.currentChanged.connect(self.on_tab_change)
        # Connect the width changed signal
        self.window_width_changed_signal.connect(self.on_window_width_changed)

        main_layout.addWidget(self.tabs)

        self.setCentralWidget(central_widget)

    @property
    def active_tab_index(self) -> int:
        return self._active_tab_index

    @active_tab_index.setter
    def active_tab_index(self, value) -> None:
        if self._active_tab_index == value:
            return
        self._active_tab_index = value
        self.tab_changed_signal.emit()

    @property
    def active_tab_widget(self) -> BaseTabWidget:
        return self.tabs.widget(self.active_tab_index)

    def create_menu_bar(self) -> None:
        menu_bar = QMenuBar(self)

        file_menu = menu_bar.addMenu("File")

        load_xml_action = QAction("Load XML", self)
        load_json_action = QAction("Load JSON", self)
        load_sqlite_action = QAction("Load SQLite", self)
        save_xml_action = QAction("Save XML", self)
        save_json_action = QAction("Save JSON", self)
        save_sqlite_action = QAction("Save SQLite", self)

        load_xml_action.triggered.connect(
            lambda: self.load_data_signal.emit(HandlerType.XML)
        )
        load_json_action.triggered.connect(
            lambda: self.load_data_signal.emit(HandlerType.JSON)
        )
        load_sqlite_action.triggered.connect(
            lambda: self.load_data_signal.emit(HandlerType.SQLITE)
        )
        save_xml_action.triggered.connect(
            lambda: self.save_data_signal.emit(HandlerType.XML)
        )
        save_json_action.triggered.connect(
            lambda: self.save_data_signal.emit(HandlerType.JSON)
        )
        save_sqlite_action.triggered.connect(
            lambda: self.save_data_signal.emit(HandlerType.SQLITE)
        )

        file_menu.addAction(load_xml_action)
        file_menu.addAction(load_json_action)
        file_menu.addAction(load_sqlite_action)
        file_menu.addSeparator()
        file_menu.addAction(save_xml_action)
        file_menu.addAction(save_json_action)
        file_menu.addAction(save_sqlite_action)

        self.setMenuBar(menu_bar)

    def on_tab_change(self, index: int) -> None:
        self.active_tab_index = index

    def on_window_width_changed(self, width: int) -> None:
        height = self.geometry().height()
        if width > self._max_window_width:
            self._max_window_width = width
        self.setGeometry(100, 100, self._max_window_width, height)
