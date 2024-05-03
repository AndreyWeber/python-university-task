from abc import ABC, abstractmethod
from typing import List

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
)
from widgets.meta_qwidget_abc import MetaQWidgetABC
from entities.general_dict import GeneralDict


class BaseTableWidget(QWidget, ABC, metaclass=MetaQWidgetABC):
    def __init__(self, headers: List[str]) -> None:
        super().__init__()
        self.headers = headers
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        self.table = QTableWidget(self)
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        self.layout.addWidget(self.table)

    @abstractmethod
    def populate_table(self, items_dict: GeneralDict) -> None:
        pass
