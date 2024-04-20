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

    @property
    def description(self):
        """Client instance string description"""
        return f"{self.surname} {self.name} {self.second_name}"

    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented

        return (
            self.name == other.name
            and self.surname == other.surname
            and self.second_name == other.second_name
        )
