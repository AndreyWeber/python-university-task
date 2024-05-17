from abc import ABC

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
from PyQt5.QtCore import pyqtSignal

from widgets.meta_qwidget_abc import MetaQWidgetABC
from widgets.base_table_widget import BaseTableWidget
from widgets.base_edit_form_widget import BaseEditFormWidget
from entities.general_dict import GeneralDict
from entities.general import General


class BaseTabWidget(QWidget, ABC, metaclass=MetaQWidgetABC):
    populate_table_widget_signal = pyqtSignal(GeneralDict)
    populate_edit_controls_widget_signal = pyqtSignal(General, dict)
    clear_edit_controls_widget_signal = pyqtSignal()
    show_warning_message_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.table_widget: BaseTableWidget = None
        self.edit_form_widget: BaseEditFormWidget = None
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        self.populate_table_widget_signal.connect(self.table_widget.populate_table)
        self.populate_edit_controls_widget_signal.connect(
            self.edit_form_widget.populate_edit_controls
        )
        self.clear_edit_controls_widget_signal.connect(
            self.edit_form_widget.clear_edit_controls
        )
        self.show_warning_message_signal.connect(self.show_warning_message_box)

        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.edit_form_widget)

    def populate_table(self, items: GeneralDict) -> None:
        if items is None:
            return
        self.populate_table_widget_signal.emit(items)

    def populate_edit_controls(self, item: General, **kwargs) -> None:
        if not item:
            return
        self.populate_edit_controls_widget_signal.emit(item, kwargs)

    def clear_edit_controls(self) -> None:
        self.clear_edit_controls_widget_signal.emit()

    def show_warning_message_box(self, message: str) -> None:
        if message is None or message.strip() == "":
            raise ValueError("'message' cannot be None or empty string")
        QMessageBox.warning(self, "Warning!", message)

    def get_code_value(self, row_index: int) -> int:
        return self.table_widget.get_code_value(row_index)
