from abc import ABCMeta

# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QWidget


class MetaQWidgetABC(type(QWidget), ABCMeta):
    pass
