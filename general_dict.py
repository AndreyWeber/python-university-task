# -*- coding:utf-8 -*-
from entities.general import General


class GeneralDict:
    def __init__(self):
        # usage of 'dict' keyword assumes Python 3.9 or later
        self._items: dict[int, General] = {}

    @property
    def item_dict(self) -> dict[int, General]:
        return self._items

    def clear(self) -> None:
        self._items.clear()

    def get_next_code(self) -> int:
        # If item_dict is empty then the first code will be 0
        return max(self.item_dict.keys(), default=-1) + 1

    def add_item(self, item: General) -> None:
        if not isinstance(item, General):
            raise TypeError(
                f"Expected an item of type 'General', but received '{type(item).__name__}'"
            )
        self.item_dict[item.code] = item

    def remove_item_by_code(self, code: int) -> None:
        if code in self.item_dict:
            del self.item_dict[code]

    def remove_item(self, item: General) -> None:
        if not isinstance(item, General):
            raise TypeError(
                f"Expected an item of type 'General', but received '{type(item).__name__}'"
            )
        self.remove_item_by_code(item.code)
