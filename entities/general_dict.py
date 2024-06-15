# -*- coding:utf-8 -*-
from typing import Dict
from entities.general import General


class GeneralDict(Dict[int, General]):
    def get_next_code(self) -> int:
        # If dict is empty then the first code will be 0
        return max(self.keys(), default=-1) + 1

    def add_item(self, item: General) -> None:
        if item.code is None:
            item.code = self.get_next_code()
        self[item.code] = item

    def remove_item_by_code(self, code: int) -> None:
        if code in self:
            del self[code]

    def remove_item(self, item: General) -> None:
        self.remove_item_by_code(item.code)
