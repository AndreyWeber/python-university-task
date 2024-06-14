from abc import ABC, abstractmethod
from typing import List

# pylint: disable=no-name-in-module
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
)
from widgets.meta_qwidget_abc import MetaQWidgetABC
from entities.general_dict import GeneralDict


class BaseTableWidget(QWidget, ABC, metaclass=MetaQWidgetABC):
    table_cell_clicked_signal = pyqtSignal(object)
    table_row_header_clicked_signal = pyqtSignal(int)

    def __init__(self, headers: List[str]) -> None:
        super().__init__()
        self.headers = headers
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        self.table = QTableWidget(self)
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        self.table.clicked.connect(self.table_cell_clicked_signal.emit)
        self.table.verticalHeader().sectionClicked.connect(
            self.table_row_header_clicked_signal.emit
        )

        self.layout.addWidget(self.table)

    @abstractmethod
    def populate_table(self, items_dict: GeneralDict) -> None:
        self.adjust_columns_size()
        # self.adjust_window_size()

    def get_item_code_value(self, row_index: int) -> int | None:
        if row_index < 0 or row_index >= self.table.rowCount():
            return None

        item = self.table.item(row_index, 0)
        if item:
            return int(item.text())
        return None

    def adjust_columns_size(self) -> None:
        self.table.resizeColumnsToContents()
        for col in range(self.table.columnCount()):
            margined_width = self.table.columnWidth(col) + 8
            self.table.setColumnWidth(col, margined_width)

    # def adjust_window_size(self) -> None:
    #     width = self.table.verticalHeader().width() + 45
    #     width += self.table.horizontalHeader().length()
    #     if self.table.verticalScrollBar().isVisible():
    #         width += self.table.verticalScrollBar().width()
    #     width += self.table.frameWidth() * 2

    #     height = self.geometry().height()

    #     self.setGeometry(100, 100, width, height)
