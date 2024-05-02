from abc import ABC, abstractmethod

# pylint: disable=no-name-in-module
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout,
    QPushButton,
)


class BaseEditFormWidget(QWidget, ABC):
    save_button_signal = pyqtSignal()
    add_button_signal = pyqtSignal()
    deelete_button_signal = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        # Create and add controls to the form layout
        self.form_layout = QFormLayout()

        self.add_edit_controls()

        self.layout.addLayout(self.form_layout)

        # Create buttons layout and add buttons
        buttons_layout = QHBoxLayout()

        self.save_button = QPushButton("Save")
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")

        # Connect buttons to their respective signals
        self.save_button.clicked.connect(self.save_button_signal.emit)
        self.add_button.clicked.connect(self.add_button_signal.emit)
        self.delete_button.clicked.connect(self.deelete_button_signal.emit)

        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.delete_button)

        self.layout.addLayout(buttons_layout)

    @abstractmethod
    def add_edit_controls(self) -> None:
        pass

    @abstractmethod
    def populate_edit_controls(self) -> None:
        pass
