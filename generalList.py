# -*- coding:utf-8 -*-
from general import General


class GeneralList:
    def __init__(self):
        self._list = []

    @property
    def list(self):
        return self._list

    def clear(self):
        self._list.clear()

    def find_by_code(self, code):
        return next((item for item in self._list if item.code == code), None)

    def get_codes(self):
        return [item.code for item in self._list]

    def append(self, value):
        if not isinstance(value, General):
            raise TypeError(
                f"Expected an element of type 'General', but received {type(value).__name__}"
            )
        self._list.append(value)

    def remove_by_code(self, code):
        self._list = [item for item in self._list if item.code != code]
