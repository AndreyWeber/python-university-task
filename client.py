# -*- coding:utf-8 -*-
from dataclasses import dataclass
from general import General


@dataclass(slots=True)
class Client(General):
    """Class representing Dry Cleaning service client"""

    name: str = ""
    surname: str = ""
    second_name: str = ""
    is_regular: bool = False

    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return NotImplemented
        return self.code == other.code
