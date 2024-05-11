from abc import ABC, abstractmethod

# pylint: disable=no-name-in-module
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout,
    QPushButton,
    QGroupBox,
)
from widgets.meta_qwidget_abc import MetaQWidgetABC
from entities.general import General


class BaseEditFormWidget(QWidget, ABC, metaclass=MetaQWidgetABC):
    add_button_signal = pyqtSignal(General)
    save_button_signal = pyqtSignal(General)
    clear_button_signal = pyqtSignal()
    delete_button_signal = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        # This statement will call initUI() in the derived class first
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        # Create and add control widgets form layout
        self.form_layout = QFormLayout()

        group_box = QGroupBox("Service Details")
        group_box.setLayout(self.form_layout)

        self.layout.addWidget(group_box)

        # Create and add buttons layout and basic buttons
        self.buttons_layout = QHBoxLayout()

        self.add_button = QPushButton("Add")
        self.save_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")
        self.delete_button = QPushButton("Delete")

        # Connect buttons to their respective signals
        self.add_button.clicked.connect(self.on_add_button_clicked)
        self.save_button.clicked.connect(self.on_save_button_clicked)
        self.clear_button.clicked.connect(self.on_clear_button_clicked)
        self.delete_button.clicked.connect(self.on_delete_button_clicked)

        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.save_button)
        self.buttons_layout.addWidget(self.clear_button)
        self.buttons_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.buttons_layout)

    @abstractmethod
    def on_add_button_clicked(self) -> None:
        pass

    @abstractmethod
    def on_save_button_clicked(self) -> None:
        pass

    @abstractmethod
    def on_clear_button_clicked(self) -> None:
        pass

    @abstractmethod
    def on_delete_button_clicked(self) -> None:
        pass

    @abstractmethod
    def populate_edit_controls(self, item: General) -> None:
        pass
