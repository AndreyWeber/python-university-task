# pylint: disable=no-name-in-module
from typing import List
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
)


class GenericTableWidget(QWidget):
    def __init__(self, headers: List[str]):
        super().__init__()
        self.headers = headers
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.table = QTableWidget(self)
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        self.layout.addWidget(self.table)
