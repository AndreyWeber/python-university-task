import sys

# pylint: disable=no-name-in-module
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QPalette, QBrush


class GrayOutDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        if index.data(Qt.UserRole) == sys.maxsize:
            option.palette.setBrush(QPalette.Text, QBrush(Qt.gray))
